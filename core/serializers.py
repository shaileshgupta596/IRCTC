from rest_framework import serializers

from core.models import Train, TrainCoaches, TrainHalts


class TrainCoachesSerializer(serializers.ModelSerializer):    
    class Meta:
        model = TrainCoaches
        fields = ['number', 'name', 'type', 'number_of_seats']


class TrainHaltsSerializer(serializers.ModelSerializer):
    station_name = serializers.CharField(source='halts.name')

    class Meta:
        model = TrainHalts
        fields = ['station_name', 'at_halt']


class TrainSerializer(serializers.ModelSerializer):
    # train_coaches = TrainCoachesSerializer(many=True,read_only=True)
    # train_halts = TrainHaltsSerializer(many=True,read_only=True)

    class Meta:
        model = Train
        fields = ['number', 'name', 'source']


class TrainCoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainCoaches
        fields = ['number', 'name', 'number_of_seats']

