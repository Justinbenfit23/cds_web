from django.shortcuts import render
from rest_framework import generics
from .models import CMC
from .serializers import CMCSerializer
from django.shortcuts import redirect, reverse
from django.views import generic
from django.contrib.auth import logout
from django.contrib.auth import logout, login, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class CMCView(generics.ListCreateAPIView):
    queryset = CMC.objects.all()
    serializer_class = CMCSerializer


 
