from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('<int:blog_id>/edit/', views.blog_edit, name='blog_update'),
    path('<int:blog_id>/delete/', views.blog_delete, name='blog_delete'),
    path('register/', views.register, name='register'),
    path('about',views.about, name='about'),
    path('contact',views.contact,name='contact')
    
  
]
