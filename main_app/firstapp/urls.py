from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register, name='register'),
    path('reg_done/', views.reg_done, name='reg_done'),
    path('login_done/', views.login_done, name='login_done'),
    path('meal_list/', views.meal_list, name='meal_list'),
    path('<int:id>', views.meal_details, name='meal_details'),
]
