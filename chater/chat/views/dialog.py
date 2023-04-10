from rest_framework import generics, status, permissions
from rest_framework.response import Response

from ..models import Dialog, Log
from ..permissions import DialogLogOwner, DialogOwner
from ..serializers import DialogSerializer, LogSerializer
from ..services import ChatService


class DialogListView(generics.ListCreateAPIView):
    serializer_class = DialogSerializer
    permission_classes = [DialogOwner, permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Dialog.objects.filter(user=self.request.user)
        return None

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DialogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DialogSerializer
    permission_classes = [DialogOwner, permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Dialog.objects.filter(user=self.request.user)
        return None


class LogListView(generics.ListCreateAPIView):
    serializer_class = LogSerializer
    permission_classes = [DialogLogOwner, permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            dialog = Dialog.objects.get(
                user=self.request.user, id=self.kwargs["dialog"]
            )
            return Log.objects.filter(dialog=dialog) if dialog else []
        return None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        chat_service = ChatService()
        log = chat_service.chat(serializer.instance)
        log_serializer = LogSerializer(instance=log)
        headers = self.get_success_headers(serializer.data)
        return Response(log_serializer.data, status=status.HTTP_200_OK, headers=headers)
