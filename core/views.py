from django.shortcuts import render
from rest_framework import generics

from core.models import Train, TrainHalts, TrainCoaches
from core.serializers import TrainSerializer, TrainCoachesSerializer, TrainCoachSerializer

# Create your views here.

class TrainListAPIView(generics.ListAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class TrainDetailAPIView(generics.RetrieveAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    lookup_field = 'number'


class TrainBetweenStationListAPIView(generics.ListAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    def get_queryset(self):
        source = self.kwargs.get('source')
        destination = self.kwargs.get('destination')
        return super().get_queryset().train_between_stations(source=source, destination=destination)
    

class TrainCoachListAPIView(generics.ListAPIView):
    queryset = TrainCoaches.objects.all()
    serializer_class = TrainCoachSerializer

    def get_queryset(self):
        train_number = self.kwargs.get('train_number')
        return super().get_queryset().filter(train__number=train_number)
    

