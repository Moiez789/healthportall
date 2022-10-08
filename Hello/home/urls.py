from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name='home'),
    path('index',views.index, name='home'),
    path('about', views.about, name='about'),
    path('post', views.post, name='post'),
    path('contact', views.contact, name='contact'),
    path('home1', views.home1, name='home1'),
]