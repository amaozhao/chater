from rest_framework import serializers

from ..models import Dialog, Log


class DialogSerializer(serializers.ModelSerializer):
    deleted = serializers.BooleanField(read_only=True)

    class Meta:
        model = Dialog
        fields = ["id", "title", "created", "updated", "deleted"]


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ["id", "dialog", "content", "source"]
