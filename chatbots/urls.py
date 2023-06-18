from django.urls import path

from . import views

urlpatterns = [
    path("", views.chats, name="chats"),
    path("chats/clear/", views.clear_chats, name="clear_chats"),
]
