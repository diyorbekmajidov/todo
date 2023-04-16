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

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    path("userlogin/", UserLogIn.as_view()),
    path('createtodo/', CreateTodo.as_view()),
    path('gettodo/<int:pk>/', TodoGetId.as_view()),
    path('updatetodo/<int:pk>/', TodoUpdate.as_view()),
    path('deletetodo/<int:pk>/', TodoDelete.as_view()),
    path('getusers/', GetAllUsers.as_view()),
]