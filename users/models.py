from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


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
        user.save(using=self.db)
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
        user.save(using=self.db)
        return user


class User(AbstractBaseUser):
    BUYER_TYPES = [
        ('Beginner', 'Beginner'),
        ('Frequent buyer', 'Frequent buyer')
    ]
    name = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=256, unique=True)
    email = models.EmailField(max_length=512)
    age = models.PositiveIntegerField(blank=False)
    activity = models.CharField(
        max_length=100,
        choices=BUYER_TYPES,
        default='Beginner'
    )
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email', 'age']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Seller(User):
    position = models.CharField(max_length=256)
    organization_name = models.CharField(max_length=512)


class Founder(Seller):
    def add_seller(self, user):
        pass

    def delete_seller(self, seller):
        pass

    def edit_position(self, seller):
        pass


class Admin(Founder):
    def create_founder(self, user):
        pass

    def block_user(self, user):
        pass

    def block_organization(self, organization):
        pass
# Create your models here.
