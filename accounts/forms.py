from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _
from .models import UserManager, User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

class UserCreationForm(forms.ModelForm):
    id = forms.CharField(
        label=_('ID'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('ID'),
                'required': 'True',
            }
        )
    )
    name = forms.CharField(
        label=_('이름'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('홍길동'),
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password confirmation'),
                'required': 'True',
            }
        )
    )
    phnum = forms.CharField(
        label=_('전화번호'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('010-1234-5678'),
                'required': 'True',
            }
        )
    )
    civnum = forms.CharField(
        label=_('주민등록번호'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('123456-1234567'),
                'required': 'True',
            }
        )
    )

    class Meta:
        model = User
        fields = ('id', 'name','phnum','civnum')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        # user.set_id(self.cleaned_data['id'])
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_('password')
    )

    class Meta:
        model = User
        fields = ('id', 'password', 'is_active', 'is_superuser','phnum')

    def clean_password2(self):
        return ""

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ( 'phnum',)

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['username', 'password']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })
