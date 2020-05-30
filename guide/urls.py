from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('mypage/', views.mypage, name ='mypage'),
    path('blog/detail/<int:pk>', views.guide_detail, name="guide_detail"),
    path('blog/delete/<int:pk>', views.guide_delete, name ="guide_delete"),
    path('blog/new', views.guide_new, name='guide_new'),
    path('blog/create', views.create, name='create'),
    path('blog/uplode/<int:pk>', views.guide_uplode, name='guide_uplode'),


]
