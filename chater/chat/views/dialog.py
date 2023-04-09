from rest_framework import generics

from ..models import Dialog, DialogLog
from ..serializers import DialogLogSerializer, DialogSerializer
from ..permissions import DialogOwner, DialogLogOwner


class DialogListView(generics.ListCreateAPIView):
    serializer_class = DialogSerializer
    permission_classes = [DialogOwner]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Dialog.objects.filter(user=self.request.user)
        return None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DialogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DialogSerializer
    permission_classes = [DialogOwner]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Dialog.objects.filter(user=self.request.user)
        return None


class DialogLogListView(generics.ListCreateAPIView):
    serializer_class = DialogLogSerializer
    permission_classes = [DialogLogOwner]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            dialog = Dialog.objects.get(
                user=self.request.user, id=self.kwargs["dialog"]
            )
            if not dialog:
                return []
            queryset = DialogLog.objects.filter(dialog=dialog)
            return queryset
        return None
