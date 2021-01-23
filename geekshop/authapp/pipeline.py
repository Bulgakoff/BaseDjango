import datetime
import os
from collections import OrderedDict
from urllib.parse import urlunparse,urlencode

import requests
from django.core.files import File
from django.utils import timezone
from social_core.exceptions import AuthForbidden

from authapp.models import ShopUserProfile, User

import urllib.request

from geekshop.settings import BASE_DIR


def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return

    print(f'============response=============>>>>>>>>{response}<<<<<<<<<')

    # api_url = f"https://api.vk.com/method/users.get/fields=bdate, sex, about,sex&access_token={response['access_token']}"
    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about','photo_400_orig')),
                                                access_token=response['access_token'],
                                                v='5.92')),
                          None
                          ))

    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    data = resp.json()['response'][0]
    if data['sex']==2:
        user.shopuserprofile.gender = ShopUserProfile.MALE
    elif data['sex']==1:
        user.shopuserprofile.gender = ShopUserProfile.FEMALE

    if data['about']:
        user.shopuserprofile.aboutMe = data['about']

    if data['bdate']:
        bdate = datetime. datetime.strptime(data['bdate'], '%d.%m.%Y').date()

    if data['photo_400_orig']:
        result = urllib.request.urlretrieve(data['photo_400_orig'],
                                            os.path.join(BASE_DIR + '/media/users_avatars',f'{user.pk}.jpg'))
        print(f'=======result======{result}==')
        # user.avatar='/media/users_avatars/' + result[0].rsplit('/', 1)[-1]
        user.avatar=f'/media/users_avatars/{user.pk}.jpg'
        user.save()
        print(f'=====----==user.avatar======{user.avatar}==')

        # result = urlretrieve(self.image_url, os.path.join(BASE_DIR + '/media/users_avatars',f'{user.pk}.jpg'))
        # self.original = '/media/users_avatars/' + result[0].rsplit('/', 1)[-1]
        # self.save()
            # (data['photo_400_orig'],f'/media/users_avatars/{user.pk}.jpg')

        print(data['photo_400_orig'])

        age = timezone.now().date().year - bdate.year
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    user.save()


