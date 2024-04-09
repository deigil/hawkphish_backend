from rest_framework import serializers
from .models import *

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = updatedLink        
        fields = ['domainURL','domainTitle','timeAccessed','domainRating',
                  'reasonNoHttps','reasonShortened','reasonAtSymbol',
                  'reasonBadExtension', 'reasonRedirect', 'reasonDashes', 'clicked_count']