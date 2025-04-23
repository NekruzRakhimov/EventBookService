from django.urls import path
from .views import MyBookingListView, CreateBookingView

urlpatterns = [
    path('', CreateBookingView.as_view(), name='create-booking'),
    path('my/', MyBookingListView.as_view(), name='my-bookings'),
]
