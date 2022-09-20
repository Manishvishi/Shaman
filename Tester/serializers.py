from .models import Vendor, Consumer
from rest_framework import serializers


class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class ConsumerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = "__all__"