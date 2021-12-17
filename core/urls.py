from django.urls import path

from . import views
urlpatterns = [
    path('door/<int:id>', views.DoorDetailView.as_view()),
]
