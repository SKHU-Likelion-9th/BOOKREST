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