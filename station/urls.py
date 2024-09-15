from django.urls import path

from station.views import FindTrainsListAPIView

app_name = 'station'

urlpatterns = [
    path('findtrains/<str:source>/<str:destination>/', FindTrainsListAPIView.as_view(), name="find-trains"),
]
