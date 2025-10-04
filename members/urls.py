from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('members/details/<int:id>/', views.details, name='details'),
    path('', views.main, name='main'),  # Added main view path
    path('testing/',views.testing,name='testing'),
]