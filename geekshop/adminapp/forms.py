from authapp.forms import UserRegisterForm, UserProfileForm, UserLoginForm
from authapp.models import User
from mainapp.models import ProductCategory
from django import forms


class UserAdminRegisterForm(UserRegisterForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'avatar', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfileForm):
    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = False
        self.fields['email'].widget.attrs['readonly'] = False


# ===================Category================================================
class CategoryAdminRegisterForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description',)
    # model = ProductCategory
    # name = forms.CharField()
    # description = forms.TimeField()


class CategoryAdminUpdateForm(CategoryAdminRegisterForm):
    def __init__(self, *args, **kwargs):
        super(CategoryAdminUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['readonly'] = False
        self.fields['description'].widget.attrs['readonly'] = False