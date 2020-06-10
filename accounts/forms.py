from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import User
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm

class UserCreationForm(forms.ModelForm): #유저 생성 뷰를 위한 폼
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

    def clean_password2(self): #비밀번호 확인 후 해싱
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True): #회원 정보 저장
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm): #유저 정보 변경 폼
    class Meta:
        model = User
        fields = ( 'name','phnum')


class LoginForm(AuthenticationForm): #로그인 폼
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_update_fields = ['username', 'password']
        for field_name in class_update_fields:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control'
            })

class UserDeleteForm(forms.ModelForm): #유저 삭제 폼
    class Meta:
        model=User
        fields = ('name',)
