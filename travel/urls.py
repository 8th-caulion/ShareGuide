from django.contrib import admin
from django.urls import path
import travel.views

urlpatterns = [
    path('tmain/', travel.views.traveler_main, name = "traveler_main"),
    path('list/', travel.views.traveler_list, name = "traveler_list"),
    path('detail/', travel.views.traveler_detail, name = "traveler_detail"),
    path('search/', travel.views.traveler_search, name = "traveler_search"),
]
