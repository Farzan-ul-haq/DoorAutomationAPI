from django.urls import path

from . import views


urlpatterns = [
    path('door/<int:id>', views.DoorDetailView.as_view()),
    path('door/<int:id>/password/', views.DoorPassword.as_view()),
    path('door/<int:id>/open/',views.OpenDoor.as_view()),
    path('door/<int:id>/close/',views.CloseDoor.as_view()),
]
