
from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register("leader", views.LeaderView)
urlpatterns = [
   
    path("home/", views.home),
    path("about/", views.about),
    path("", include(router.urls)),
   
]



