from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('passenger', 'Passenger'),
        ('driver', 'Driver'),
        ('admin', 'Admin')
    )

    # other attributes
    # you don't need to redefine fields inherited from your base class
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='passenger')

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % self.pk

    def get_email(self):
        return self.email

    @property
    def is_passenger(self):
        return self.role == 'passenger'

    @property
    def is_driver(self):
        return self.role == 'driver'


# view function
# @login_required
# def index(request, *args, **kwargs):
#     if request.user.is_passenger:
#         #do something
#     elif request.user.is_driver:
#         #do something other

class UserType(models.Model):
    is_driver = models.BooleanField(default=False)
    is_passenger = models.BooleanField(default=False)
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)

    def __str__(self):
        if self.is_passenger:
            return AppUser.get_email(self.user) + " - is_student"
        else:
            return AppUser.get_email(self.user) + " - is_teacher"
