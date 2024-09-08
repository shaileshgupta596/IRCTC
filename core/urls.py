from django.urls import path
from core.views import (
    TrainListAPIView, 
    TrainDetailAPIView,
    TrainBetweenStationListAPIView
)

app_name = 'core'

urlpatterns = [
    path('listTrains', TrainListAPIView.as_view(), name='list-train'),
    path('retriveTrain/<str:number>/', TrainDetailAPIView.as_view(), name='retrive-train'),
    path('listTrains/<str:source>/<str:destination>', TrainBetweenStationListAPIView.as_view(), name="train-source-destination")
]
