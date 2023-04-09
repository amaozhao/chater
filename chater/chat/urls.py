from django.urls import path

from .views import DialogDetailView, DialogListView, LogListView

urlpatterns = [
    path("dialogs/", DialogListView.as_view(), name="dialog-list"),
    path("dialogs/<int:pk>/", DialogDetailView.as_view(), name="dialog-detail"),
    path("<int:dialog>/logs/", LogListView.as_view(), name="log-list"),
]
