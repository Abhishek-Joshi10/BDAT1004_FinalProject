from rest_framework import serializers

from .models import Product_Delhi

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product_Delhi
        fields = ('temp','feels_like','temp_min','temp_max')