from django.urls import path

from .views import DialogDetailView, DialogListView, DialogLogListView

urlpatterns = [
    path("dialogs/", DialogListView.as_view()),
    path("dialogs/<int:pk>/", DialogDetailView.as_view()),
    path("dialoglogs/<int:dialog>/", DialogLogListView.as_view()),
]
