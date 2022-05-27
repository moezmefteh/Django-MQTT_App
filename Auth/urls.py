from django.urls import path
from .views import LoginView, UserView, LogoutView, PropertiesUserUpdate, UsersDefineAll

urlpatterns = [
    path('users/',UsersDefineAll.as_view()),

    path('login/', LoginView.as_view()),

    path('user/', UserView.as_view()),

    path('logout/', LogoutView.as_view()),

    path('update/<str:pk>/',PropertiesUserUpdate.as_view()),

    

    
]