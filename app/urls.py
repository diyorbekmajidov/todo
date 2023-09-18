from .views import (
    CreateUserView, 
    UserLogOut,
    UserLogIn,
    CreateTodo, 
    TodoGetId, 
    TodoUpdate, 
    TodoDelete, 
    GetAllUsers)
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    path("userlogin/", UserLogIn.as_view()),
    path('createtodo/', CreateTodo.as_view()),
    path('gettodo/<int:pk>/', TodoGetId.as_view()),
    path('updatetodo/<int:pk>/', TodoUpdate.as_view()),
    path('deletetodo/<int:pk>/', TodoDelete.as_view()),
    path('getusers/', GetAllUsers.as_view()),
    path('gettoken/', obtain_auth_token, name='api_token_auth'),
]