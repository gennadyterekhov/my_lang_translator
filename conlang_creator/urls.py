from django.urls import path
from . import views

app_name = 'conlang_creator'
urlpatterns = [
    path('create/', views.create, name='create'),
    path('create/check', views.create_check, name='create_check'),
    path('<int:conlang_id>/profile/', views.profile, name='profile'),
    path('list/', views.conlang_list, name='list'),
]
