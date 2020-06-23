

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register("leader", views.LeaderView)

urlpatterns = [
	path('', views.home, name="home"), 
	path('about/', views.about, name="about"), 
	path('contact.html', views.contact, name="contact"),

 	path('api/', include(router.urls)),
   
]



