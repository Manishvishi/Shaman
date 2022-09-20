from .models import Vendor, Consumer
# from django_filters import rest_framework as filters
import django_filters
from django.db.models import Q

class VendorFilterSet(django_filters.FilterSet):
    merge = django_filters.CharFilter(method="person_detail")
    class Meta:
        model = Vendor
        fields = {
            "id": ["exact", "in"],
            "name": ["exact","icontains"],
            "city": ["exact", "icontains"]
        }

    def person_detail(self, queryset, name, value):
        filter = {}
        print(value)
        if value:
            queryset = queryset.filter( Q(name=value) | Q(city=value) )
        return queryset


class ConsumerFilterSet(django_filters.FilterSet):

    class Meta:
        model = Consumer
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "city": ["exact", "icontains"]
        }