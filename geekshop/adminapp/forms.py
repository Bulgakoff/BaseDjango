from authapp.forms import UserRegisterForm, UserProfileForm, UserLoginForm
from authapp.models import User
from mainapp.models import ProductCategory,Products
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


class CategoryAdminUpdateForm(CategoryAdminRegisterForm):
    def __init__(self, *args, **kwargs):
        super(CategoryAdminUpdateForm, self).__init__(*args, **kwargs)


# ===================Products================================================
class ProductAdminRegisterForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = Products
        fields = ('name', 'image', 'description', 'short_description', 'price', 'guantity', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductAdminRegisterForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductAdminUpdateForm(ProductAdminRegisterForm):
    def __init__(self, *args, **kwargs):
        super(ProductAdminUpdateForm, self).__init__(*args, **kwargs)