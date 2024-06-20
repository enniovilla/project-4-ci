from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
]