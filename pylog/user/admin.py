from django.contrib import admin
from user.models import User


@admin.register(User)
class User(admin.ModelAdmin):
    pass
