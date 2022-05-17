from django.contrib import admin
from django.contrib.auth import get_user_model
from stu_task import settings
# Register your models here.
admin.site.register(get_user_model())

# admin.site.register(settings.AUTH_USER_MODEL)
