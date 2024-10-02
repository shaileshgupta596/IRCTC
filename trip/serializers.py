from rest_framework import serializers
from core.models import Train

from trip.models import TrainSeatAvailable


class TrainSeatAvailableSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = TrainSeatAvailable
        fields = ['train', 'seats', 'url']

    def get_url(self, obj):
        return obj.get_absolute_url()
    

class TrainSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField() 

    class Meta:
        model = Train
        fields = ['name', 'number', 'source', 'destination', 'url']

    def get_url(self, obj):
        return f"/{obj.pk}"





