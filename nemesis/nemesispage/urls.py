from django.contrib import admin
from django.urls import path
from nemesispage import views

urlpatterns = [
    path('', views.login,name='login'),
    path('regis/', views.regis,name='regis'),
    path('get/', views.get,name='get/'),
    path('authen/', views.authen,name='authen/'),
    path('home/<str:name>', views.home,name='home/'),
    path('ser/', views.ser,name='ser/'),
    path('update/', views.update,name='update/'),

]