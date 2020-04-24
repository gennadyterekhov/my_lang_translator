from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('in/', views.login, name='registration_login'),
    path('in/check/', views.login_check, name='registration_login_check'),
    path('up/', views.register, name='registration_register'),
    path('up/check/', views.register_check, name='registration_register_check'),
    
]
