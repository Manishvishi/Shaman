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

    # def validate(self, attrs):
    #     name = attrs.get("name")

    #     if len(name) <= 4:
    #         raise serializers.ValidationError(f"{name} must more then 4 character")
    #     return attrs