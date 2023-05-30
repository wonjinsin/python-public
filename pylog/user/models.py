from django.db import models


class User(models.Model):
    uid = models.IntegerField()
