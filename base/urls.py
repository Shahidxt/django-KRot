from django.urls import path
from django.contrib import admin
from . import views

 
urlpatterns = [
    path('',views.index,name="home"),
    path("register",views.registerUser, name="register"),
    path("room/<str:pk>/",views.room, name='room'),
    path("createroom/", views.CreateRoom, name= 'createroom'),
    path("update/<str:pk>/",views.Updateform, name= 'updateform'),
    path("Delete/<str:pk>", views.deleteRoom,name='delete'),
    path('Login',views.Login_form,name="login"),
    path('Logout',views.LogoutUser, name='logout'),
    path("delMassage/<str:pk>",views.DeleteMassage,name="delete-massage"),
    path("Profile/<str:pk>", views.UserProfile ,name='profile'),
    path('settings/',views.settings,name="settings"),
    path("topics/",views.TopicsTemp,name='topics'),
    path('activitys/',views.ActivityTemp,name='activity'),
     path('createtopic/',views.Topic_Create,name='createtopic'),
]
