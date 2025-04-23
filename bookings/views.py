from rest_framework import permissions, generics

from .serializers import BookingSerializer, CreateBookingSerializer
from .models import Booking


# Create your views here.
class MyBookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)


class CreateBookingView(generics.CreateAPIView):
    serializer_class = CreateBookingSerializer
    permission_classes = [permissions.IsAuthenticated]
