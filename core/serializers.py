from rest_framework import serializers

from core.models import Train, TrainCoaches

class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = '__all__'