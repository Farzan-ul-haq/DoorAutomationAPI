from django.urls import path

from . import views


urlpatterns = [
    path(
        'door/<int:id>/',
        views.DoorDetailView.as_view(),
        name='door-api-detail'
    ),
    path(
        'door/',
        views.DoorListView.as_view(),
        name='door-list'    
    ),
    path(
        'door/<int:id>/password/', 
        views.DoorPasswordView.as_view(),
        name='door-password'    
    ),
    path(
        'door/<int:id>/status/',
        views.DoorStatusView.as_view(),
        name='door-status'
    ),
]
