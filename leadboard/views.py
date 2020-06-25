from django.shortcuts import render
from rest_framework import viewsets 
from .models import Leader
from .models import Members
import requests
import json


from . import serializers
from .serializers import (
    LeaderSerializer,
   
)
# Create your views here.
class LeaderView(viewsets.ModelViewSet):
    """Handles Listing leader."""

    serializer_class = serializers.LeaderSerializer
    queryset = Leader.objects.all()

def home(request):
    #context = {"leaders":Leader.objects.all()}
    member = Members.objects.all()
    return render(request, "home.html", {'member': member})


def about(request):
    return render(request, "about.html", {"title": "About"})

def contact(request):
	 member = Members.objects.all()
	 return render(request, 'contact.html', {})



