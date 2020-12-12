from django.contrib import admin
from django.urls import path

from newsapp import views
from newsapp import views1
from newsapp import views2
from newsapp import views3
from newsapp import views4
from newsapp import views5
from newsapp import views6


urlpatterns = [
    path("", views.bbc, name="home"),
    path("hindu", views1.hindu, name="hindu"),
    path("toi", views2.toi, name="toi"),
    path("india", views3.india, name="india"),
    path("business", views4.business, name="business"),
    path("tech", views5.tech, name="tech"),
    path("sports", views6.sports, name="sports"),
]