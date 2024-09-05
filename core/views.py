from django.shortcuts import render
from rest_framework import generics

from core.models import Train
from core.serializers import TrainSerializer

# Create your views here.

class TrainListAPIView(generics.ListAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class TrainDetailAPIView(generics.RetrieveAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    lookup_field = 'number'

