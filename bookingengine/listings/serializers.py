
from collections import OrderedDict
from django.db.models import fields 
from .models import BookedListing, BookingInfo, Listing
from rest_framework import serializers
from operator import itemgetter

class HotelSerializer(serializers.Serializer):
    
    class Meta:
        model = Listing
    
    
    
    
class ListingSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Listing
        fields = ("listing_type",
                "title",
                "country",
                "city")
        
        
class BookingInfoSerializer(serializers.ModelSerializer):
    listing = ListingSerializer()
    class Meta:
        model = BookingInfo
        fields = ("__all__")
        depth = 2
        
        
    # def get_listing_type(self,obj):
    #     if obj.listing_type is None:
    #         listing_type = 'hotel'
    #         return listing_type
    #     listing_type = obj.listing_type
    #     return listing_type
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret
        
        
class BookedListingSerializer(serializers.ModelSerializer):
    # booking_info = ListingSerializer()
    class Meta:
        model = BookedListing
        # fields = ('listing',)
        fields = ("booking_info",)
        depth = 3
        
        def to_representation(self, instance):
            ret = super().to_representation(instance)
            ret = OrderedDict(filter(itemgetter(1), ret.items()))
            return ret