from datetime import date, datetime, timedelta

from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


from core.models import Train, TrainCoaches, TrainHalts
from trip.models import TrainSeatAvailable
from trip.serializers import TrainSerializer, TrainSeatAvailableSerializer
from station.utils import train_between_two_stations


# Create your views here.


class TrainRetriveView(RetrieveAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer
    lookup_field = 'number'


class TrainListAPIView(ListAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer


    def get_queryset(self):
        src = self.kwargs.get('src')
        dest = self.kwargs.get('dest')
        trip_date = self.kwargs.get('trip_date')
        trip_date = datetime.strptime(trip_date, '%d-%m-%Y')
        if trip_date < datetime.today():
            return []
        if trip_date > (datetime.today() + timedelta(days=30)):
            return []
        return train_between_two_stations(src, dest)
    

class SeatAvalabilityRetriveAPIView(ListAPIView):
    queryset = TrainSeatAvailable.objects.all()
    serializer_class = TrainSeatAvailableSerializer

    def get_queryset(self):
        train_number = self.kwargs.get('train')
        trip_date = self.kwargs.get('trip_date')
        return super().get_queryset().filter(train__number=int(train_number), date=trip_date)




