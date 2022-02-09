from django.shortcuts import render
from rest_framework import generics
from .models import CMC
from .serializers import CMCSerializer
# Create your views here.

class CMCView(generics.ListCreateAPIView):
    queryset = CMC.objects.all()
    serializer_class = CMCSerializer