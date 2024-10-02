from django.urls import path

from trip.views import (TrainListAPIView,TrainRetriveView, SeatAvalabilityRetriveAPIView)

app_name = 'trip'

urlpatterns = [
    path('retrive/<int:number>/', TrainRetriveView.as_view(), name="retrive-train"),
    path('list/<str:src>/<str:dest>/<str:trip_date>/', TrainListAPIView.as_view(), name='list-trains'),
    path('list_seats/<int:train>/<str:trip_date>/', SeatAvalabilityRetriveAPIView.as_view(), name='list-seats'),
]
