
import datetime
from urllib import response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import  api_view, permission_classes 
# renderer_classes
from rest_framework import status

from django.db.models import Q
from rest_framework import generics, status, views, permissions

from listings.serializers import BookedListingSerializer, BookingInfoSerializer, ListingSerializer
# from .serializers import 
from .models import BookedListing, Listing,BookingInfo,HotelRoom
# Create your views here.


        
@api_view(['GET'])
def get_available_listings(request):
    if not request.query_params:
        
        booked = BookedListing.objects.all()
        serializer = BookedListingSerializer(booked,many=True)
        response = Response()
        response.data = {
            'data':serializer.data
        }
        return response
    if request.query_params.get('max_price'):
        if request.query_params.get('check_in') :
            if request.query_params.get('check_out') :
                price = request.query_params.get('max_price')
                check_in = request.query_params.get('check_in')
                check_out = request.query_params.get('check_out')
                response = Response()
                start_d =datetime.datetime.strptime(check_in, '%Y-%m-%d')
                end_d =datetime.datetime.strptime(check_out, '%Y-%m-%d')
                listing = BookedListing.objects.filter(booking_info__price__lte=price).exclude(booking_start_date__range =(start_d,end_d))
                serializer =  BookedListingSerializer(listing,many=True)
                response.data={
                    'status': status.HTTP_200_OK,
                    'data':serializer.data
                }
                return response
    
    
    
    
    
    
    
#     # listing = 
    
    
# # #     return response



# class BookingInfoViewSet(generics.ListAPIView):
#     """
#     BookingInfoViewSet
#     """
#     serializer_class = BookingInfoSerializer

#     def get_queryset(self):
#         max_price = self.request.query_params.get('max_price')
#         check_in = self.request.query_params.get('check_in')
#         check_out = self.request.query_params.get('check_out')
#         print(max_price, check_in, check_out)
#         queryset = BookingInfo.objects.all()
#         if max_price:
#             queryset.filter(price__lte=max_price)
#         if check_in and check_out:
#             reserved_listing = BookedListing.objects.filter(Q(Booking_start_date__lte=check_in, booking_start_date__gte=check_in) | Q(booking_end_date__lte=check_out, booking_end_date__gte=check_out))
#             print(len(reserved_listing))

#             queryset = queryset.exclude(id__in=[item.booking_info.id for item in reserved_listing])
#         return queryset.order_by('price')
    



# class BookedListingViewSet(generics.ListCreateAPIView):
   
#     serializer_class = BookedListingSerializer
#     queryset = BookedListing.objects.all()