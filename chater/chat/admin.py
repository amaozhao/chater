from django.contrib import admin

from .models import Dialog, DialogLog


@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    pass


@admin.register(DialogLog)
class DialogLogAdmin(admin.ModelAdmin):
    pass
