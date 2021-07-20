from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _

from .models import CustomUser, UserManager

class UserCreationForm(forms.ModelForm):
    # 사용자 생성 폼
    email = forms.EmailField(
        label=_('이메일'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Email address'),
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label=_('비밀번호'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label=_('비밀번호 확인'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('비밀번호 확인'),
                'required': 'True',
            }
        )
    )
    username = forms.CharField(
        label=_('이름'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('이름'),
                'required': 'True',
            }
        )
    )
    department = forms.CharField(
        label=_('학과'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('학과'),
                'required': 'True',
            }
        )
    )
    # phone_number = forms.IntegerField(
    #     label=_('전화번호'),
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': _('전화번호'),
    #             'required': 'True',
    #         }
    #     )
    # )
    birth = forms.DateField(
        label=_('생년월일'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('생년월일'),
                'required': 'True',
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ('email','username','department','student_id','birth')

    def clean_password2(self):
        # 두 비밀번호 입력 일치 확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 맞지 않습니다. 다시 입력해주세요.")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # 비밀번호 변경 폼
    password = ReadOnlyPasswordHashField(
        label=_('Password')
    )

    class Meta:
        model = CustomUser
        fields = ('email','password','username','department','student_id','birth','is_active','is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]