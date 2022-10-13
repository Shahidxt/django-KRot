from django.urls import path

from . import views

urlpatterns=[
    path('',views.getRoutes),
    path("rooms/",views.getRooms),
     path("room/<int:pk>",views.getRoom),
     path("messages/",views.Get_Messages),
     path("users/<pk>",views.GET_USERS),
]