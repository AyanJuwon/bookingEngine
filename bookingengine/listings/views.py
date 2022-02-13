
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
                    'data':serializer.data,
                }
                return response
    
    
    
    