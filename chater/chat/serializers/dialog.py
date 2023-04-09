from django.urls import reverse
from rest_framework import serializers

from ..models import Dialog, Log


class LogsUrlField(serializers.Field):
    def to_representation(self, value):
        return value

    def get_attribute(self, instance):
        return reverse("log-list", args=[instance.id])


class DialogSerializer(serializers.ModelSerializer):
    deleted = serializers.BooleanField(read_only=True)
    logs_url = LogsUrlField(read_only=True)

    class Meta:
        model = Dialog
        fields = ["id", "title", "created", "updated", "deleted", "logs_url"]


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ["id", "dialog", "content", "source"]
