from rest_framework import serializers

from core.models import Train, TrainCoaches


class TrainCoachesSerializer(serializers.ModelSerializer):    
    class Meta:
        model = TrainCoaches
        fields = ['number', 'name', 'type', 'number_of_seats']


class TrainSerializer(serializers.ModelSerializer):
    # train_coaches = TrainCoachesSerializer(many=True,read_only=True)

    class Meta:
        model = Train
        fields = ['number', 'name', 'source', 'destination']