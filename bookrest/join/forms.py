from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from .models import CustomUser, UserManager
from .choices import *

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    # 사용자 생성 폼
    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2", "username", "major", "student_id", "phone_number")

    # def clean_password2(self):
    #     # 두 비밀번호 입력 일치 확인
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("비밀번호가 맞지 않습니다. 다시 입력해주세요.")
    #     return password2

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.email = UserManager.normalize_email(self.cleaned_data['email'])
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user


class UserChangeForm(forms.ModelForm):
    # 비밀번호 변경 폼
    password = ReadOnlyPasswordHashField(
        label=('Password')
    )

    class Meta:
        model = CustomUser
        fields = ('email','password',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]