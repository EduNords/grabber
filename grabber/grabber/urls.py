from django.contrib import admin
from django.urls import path    
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('grabber/', views.grabber_page, name='grabber'),
    path('grabbers/create/', views.grabber_create, name='grabber_create'),
    path("criar-superuser/", views.criar_superuser, name='criar_superuser'),
]
