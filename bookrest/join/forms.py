from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import CustomUser, UserManager
from .choices import *
class UserCreationForm(forms.ModelForm):
    # 사용자 생성 폼
    email = forms.EmailField(
        label=('이메일'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Email address'),
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label=('비밀번호'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Password'),
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label=('비밀번호 확인'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('비밀번호 확인'),
                'required': 'True',
            }
        )
    )
    name = forms.CharField(
        label=('이름'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('이름 입력'),
                'required': 'True',
            }
        )
    )
    phone_number = forms.CharField(
        label=('전화번호'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('010-XXXX-XXXX로 작성'),
                #'required': 'True',
            }
        )
    )
    birth = forms.DateField(
        label=('생년월일'),
        required=True,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('생년월일'),
                #'required': 'True',
            }
        )
    )
    major = forms.ChoiceField(
        label=('학과'),
        required=True,
        choices=MAJOR,
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-control',
                'placeholder': ('학과'),
                #'required': 'True',
            }
        )
    )
    student_id  = forms.CharField(
        label=('학번'),
        required=True,
        
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('ex) 201810102'),
                #'required': 'True',
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ('email','name','major','student_id','birth','phone_number')

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
        label=('Password')
    )

    class Meta:
        model = CustomUser
        fields = ('email','password','name','major','student_id','birth','phone_number','is_active','is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]