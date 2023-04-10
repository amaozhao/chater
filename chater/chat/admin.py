from django.contrib import admin

from .models import Dialog, Log, Profile


@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    pass


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
