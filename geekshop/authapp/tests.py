from django.conf import settings
from django.test import TestCase, Client

from authapp.models import User
from mainapp.models import Products


class TestUserAuthTestCase(TestCase):
    username = 'django'
    email = 'dj@gb.local'
    password = 'geekbrains'

    def setUp(self):
        self.admin = User.objects.create_superuser(self.username, self.email, self.password)
        self.client = Client()

    def test_user_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_anonymous)  # тут проверяем что пользователь НЕ залогинен
        self.assertNotContains(response, 'Пользователь')  # в респосе нет слова пользователь

        # вводим  данные пользователя
        self.client.login(username=self.username, password=self.password)
        # после  на странице /login/
        response = self.client.get('/auth/login/')
        self.assertFalse(response.context['user'].is_anonymous)  # тут проверяем что пользователь Залогинен
        self.assertEqual(response.context['user'], self.admin)  # тут пользователь == admin
        # главная после логина
        response = self.client.get('/')
        self.assertFalse(response.context['user'].is_anonymous)  # тут проверяем что пользователь Залогинен
        self.assertContains(response, 'Пользователь')

    def test_profile_basket_login_redirect(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get('/auth/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['baskets']), [])

    def test_user_regisetr(self):
        response = self.client.get('/auth/register/')
        self.assertEqual(response.status_code, 200)

        new_user_data = {
            'username': 'django2',
            'first_name': 'Сэмюэл',
            'last_name': 'Джексон',
            'password1': self.password,
            'password2': self.password,
            'email': 'django2@gb.local'
        }
        # отправляем запрос
        response = self.client.post('/auth/register/', data=new_user_data)
        self.assertEqual(response.status_code,
                         302)  # редирект == 302 == return HttpResponseRedirect(reverse('auth:login'))

        new_user = User.objects.get(username='django2')
        activation_url = f"{settings.DOMAIN_NAME}/auth/verify/{new_user_data['email']}/{new_user.activation_key}/"

        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, 302)

        # данные нового пользователя
        self.client.login(username=new_user_data['username'],
                          password=new_user_data['password1'])

        # логинимся
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_anonymous)

        # проверяем главную страницу   с наличием имеени пользователя
        response = self.client.get('/')
        self.assertContains(response, text=new_user_data['first_name'],
                            status_code=200)

    def test_user_wrong_register(self):
        new_user_data = {
            'username': 'teen',
            'first_name': 'Мэри',
            'last_name': 'Поппинс',
            'password1': 'geekbrains',
            'password2': 'geekbrains',
            'email': 'merypoppins.local',
            }

        response = self.client.post('/auth/register/', data=new_user_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'UserRegisterForm', 'email',
                             'Чтото не так в мыле')
