from django.shortcuts import render
# from rest_framework.response import JsonResponse
from Tester.serializers import consumerSerializer, vendorSerializer
from .models import vendor, consumer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.



class vendorList(APIView):
    def get(self, request):
        Vendor = vendor.objects.all()
        serializer = vendorSerializer(Vendor, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = vendorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    

class vendorDetail(APIView):
    def get_object(self, pk):
        try:
            return vendor.objects.get(pk=pk)
        except vendor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vendor = self.get_object(pk)
        serializer = vendorSerializer(vendor)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        Vendor = vendor.objects.all()
        Vendor = self.get_object(Vendor, pk=pk)
        serializer = vendorSerializer(Vendor)
        return Response(serializer.data)

    def put(self, request, pk):
        vendor = self.get_object(pk)
        serializer = vendorSerializer(vendor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vendor = self.get_object(pk)
        vendor.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class consumerList(APIView):
    def get(self, request):
        Consumer = consumer.objects.all()
        serializer = consumerSerializer(Consumer, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = consumerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    

class consumerDetail(APIView):
    def get_object(self, pk):
        try:
            return consumer.objects.get(pk=pk)
        except consumer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        consumer = self.get_object(pk)
        serializer = consumerSerializer(consumer)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        Consumer = consumer.objects.all()
        Consumer = self.get_object(Consumer, pk=pk)
        serializer = consumerSerializer(Consumer)
        return Response(serializer.data)

    def put(self, request, pk):
        consumer = self.get_object(pk)
        serializer = consumerSerializer(consumer, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        consumer = self.get_object(pk)
        consumer.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
