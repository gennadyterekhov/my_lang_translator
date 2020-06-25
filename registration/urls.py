from django.urls import path
from . import views


app_name = 'registration'
urlpatterns = [
    path('in/', views.login, name='login'),
    path('in/check/', views.login_check, name='login_check'),
    path('up/', views.register, name='register'),
    path('up/check/', views.register_check, name='register_check'),
    path('logout/', views.logout, name='logout'),
]
