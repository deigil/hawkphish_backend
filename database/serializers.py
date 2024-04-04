from rest_framework import serializers
from .models import *

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['domainURL','domainTitle','timeAccessed','domainRating',
                  'reasonNoHttps','reasonShortened','reasonAtSymbol',
                  'reasonBadExtension', 'clicked_count']
        
        model = updatedLink        
        fields = ['domainURL','domainTitle','timeAccessed','domainRating',
                  'reasonNoHttps','reasonShortened','reasonAtSymbol',
                  'reasonBadExtension', 'reasonRedirect', 'reasonDashes', 'clicked_count']