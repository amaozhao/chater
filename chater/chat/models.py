from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _


class Dialog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    title = models.CharField(_("title"), max_length=128)
    created = models.DateTimeField(_("created"), auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    deleted = models.BooleanField(_("deleted"), default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "dialog"
        indexes = [
            models.Index(fields=["title"], name="chat_dialog_title"),
            models.Index(fields=["created"], name="chat_dialog_created"),
        ]
        verbose_name = _("dialog")
        verbose_name_plural = _("dialogs")


class DialogLog(models.Model):
    REQUEST = "Quest"
    RESPONSE = "Response"
    _CHOICES = [
        (REQUEST, "Request"),
        (RESPONSE, "Response"),
    ]
    dialog = models.ForeignKey(
        Dialog, on_delete=models.CASCADE, verbose_name=_("dialog")
    )
    content = models.TextField(_("content"))
    source = models.CharField(
        _("source"), max_length=16, choices=_CHOICES, default=REQUEST
    )
    created = models.DateTimeField(_("created"), auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    deleted = models.BooleanField(_("deleted"), default=False)

    def __str__(self):
        return f"{self.dialog.title}-{self.source}-{self.content[: 20]}-{self.created}"

    class Meta:
        db_table = "dialog_log"
        indexes = [
            models.Index(fields=["source"], name="chat_dialog_log_source"),
            models.Index(fields=["created"], name="chat_dialog_log_created"),
        ]
        verbose_name = _("dialog log")
        verbose_name_plural = _("dialog logs")
