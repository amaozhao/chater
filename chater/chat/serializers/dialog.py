from rest_framework import serializers

from ..models import Dialog, DialogLog


class DialogSerializer(serializers.ModelSerializer):
    deleted = serializers.BooleanField(read_only=True)

    class Meta:
        model = Dialog
        fields = ["id", "title", "created", "updated", "deleted"]


class DialogLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DialogLog
        fields = ["id", "dialog", "content", "source"]
