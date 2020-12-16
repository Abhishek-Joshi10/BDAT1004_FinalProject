from rest_framework import serializers

from .models import Product_Delhi, Product_Chennai, Product_Bangalore, Product_Hyderabad, Country


class DPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = ('index','city','temp', 'feels_like', 'temp_min', 'temp_max')

