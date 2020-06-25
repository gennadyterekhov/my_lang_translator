from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('<int:user_id>/profile/', views.profile, name='profile'),
    # path('profile/', views.profile, name='profile'),
    path('list/', views.user_list, name='list'),
    
]
