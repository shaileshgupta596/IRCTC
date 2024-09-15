from django.shortcuts import render
from rest_framework.generics import ListAPIView
# Create your views here.

from core.models import Train
from core.serializers import TrainSerializer
from station.utils import train_between_two_stations

class FindTrainsListAPIView(ListAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer

    def get_queryset(self):
        src = self.kwargs.get('source')
        dest = self.kwargs.get('destination')
        return train_between_two_stations(src, dest)
