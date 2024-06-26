from django.urls import path
from .import views


urlpatterns = [

    path('', views.viewHome, name=""),

    path('register', views.register, name="register"),

    path('login', views.login, name="login"),

    path('user_logout', views.user_logout, name="user_logout"),

    path('dashboard', views.dashboard, name="dashboard"),

    path('update_tasks<str:pk>/', views.updateTasks, name="update_tasks"),

    path('delete_tasks<str:pk>/', views.deleteTasks, name="delete_tasks"),

]
