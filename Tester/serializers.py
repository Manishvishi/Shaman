from rest_framework import serializers
from Tester.models import vendor, consumer

class vendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor
        fields = ['name', 'city']

class consumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = consumer
        fields = ['name', 'city', 'product']