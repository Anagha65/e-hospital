from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.Register_user,name='registers'),
    path('login',views.loginUser, name='login'),
    path('logout/',views.logOut, name='logout'),
    path(' ',views.HomePage,name='user_home')

]
