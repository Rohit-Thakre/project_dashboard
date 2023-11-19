from django.shortcuts import render
from rest_framework import viewsets
from main.models import Data
from API.serializers import DataSerializer
from rest_framework.response import Response


class DataViewSet(viewsets.ModelViewSet): 
    queryset = Data.objects.all()
    serializer_class = DataSerializer
