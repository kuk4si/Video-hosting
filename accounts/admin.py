from django.contrib import admin
from .models import User


# Register your models here.


class AdminInterface(admin.ModelAdmin):

    list_display = ('username', 'password', 'age', 'is_staff')


admin.site.register(User, AdminInterface)
