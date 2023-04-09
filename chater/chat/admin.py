from django.contrib import admin

from .models import Dialog, Log


@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    pass


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    pass
