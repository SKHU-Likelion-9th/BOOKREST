from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils import timezone
from .choices import *

# Create your models here.
class UserManager(BaseUserManager):    
   
    use_in_migrations = True    
   
    #유저 생성
    #파라미터로 전달받은 값들을 user 객체로 db에 저장한다
    def _create_user(self, email, name, password, **extra_fields):   
        if not email:            
            raise ValueError('이메일을 반드시 입력해주세요.')
        if not password:            
            raise ValueError('비밀번호를 반드시 입력해주세요.')    
        email = self.normalize_email(email)
        user = self.model(email = email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)        
        return user

    #일반 유저 생성
    # is_staff, is_superuser = False -> 일반 유저
    def create_user(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, password,  **extra_fields)

    #슈퍼 유저
    def create_superuser(self, email, name,password, **extra_fields):        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('관리자는 is_staff가 True여야함')
        if not extra_fields.get('is_superuser'):
            raise ValueError('관리자는 is_superuser가 True여야함')

        return self._create_user(email, name, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
   
    objects = UserManager()

    salt = models.CharField(
        verbose_name=('Salt'),
        max_length=10,
        blank=True
    )
   
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=20,unique=True)
    major = models.CharField(choices=MAJOR, max_length=30,null=True)
    phone_number = models.CharField(max_length=20,null=True)
    birth = models.DateField('birth', null=True)
    student_id = models.CharField(max_length=20,null=True)
    #no_borrow_period
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'name'    
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.name

#    @property
#    def is_staff(self):
#        return self.is_superuser
