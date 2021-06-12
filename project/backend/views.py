from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework import generics


# Create your views here.

class Test(generics.ListCreateAPIView):
    # queryset = .objects.all()
    # serializer_class = Serializer
    pass
