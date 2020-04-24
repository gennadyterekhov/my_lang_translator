from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('in/', views.login, name='registration_login'),
    path('up/', views.register, name='registration_register'),
]
