from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_image = models.ImageField(
        '프로필 이미지', upload_to='users/profiles', blank=True)
    short_description = models.TextField('소개글', blank=True)
    pass
