from django.db.models import Sum
from core.models import Train, TrainCoaches

def run():
    train = Train.objects.last()
    train_seats = TrainCoaches.objects.filter(train=train).values('type').annotate(seats=Sum('number_of_seats'))
    seats = {}
    for object in train_seats:
        seats[object.get('type')] = object.get('seats')
    print(seats)
