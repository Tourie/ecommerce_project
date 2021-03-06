from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
import logging

logger = logging.getLogger()



class MyUserManager(BaseUserManager):
    def create_user(self, name, username, email, age, password=None):
        if not name:
            raise ValueError('User must have name')
        if not email:
            raise ValueError('User must have email')
        if not username:
            raise ValueError('User must have username')
        if not age or age <= 3:
            raise ValueError('User must have age')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
            age=age,
        )
        user.set_password(password)
        user.verify = False
        user.save(using=self.db)
        logger.warning(f'Пользователь {username} зарегистрировался на сайте')
        return user

    def create_superuser(self, name, username, email, age, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            name=name,
            age=age,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.verify = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    BUYER_TYPES = [
        ('Начинающий', 'Начинающий'),
        ('Опытный покупатель', 'Опытный покупатель')
    ]
    name = models.CharField(max_length=100, blank=False, verbose_name='Имя', null=True)
    username = models.CharField(max_length=256, unique=True, verbose_name='Никнейм')
    email = models.EmailField(max_length=512, unique=True)
    age = models.PositiveIntegerField(blank=False, verbose_name="Возраст", default=18)
    activity = models.CharField(
        max_length=100,
        choices=BUYER_TYPES,
        default='Начинающий'
    )
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    verify = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'age']

    class Meta:
        indexes = [
            models.Index(fields=['username', 'email'])
        ]

    def __str__(self):
        return self.username

    @property
    def has_perm(self, obj=None):
        return self.is_admin

    @property
    def has_valid_age(self):
        return self.age > 5

    @property
    def test_person(self):
        return self.name, self.username, self.email, self.age, self.activity

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
