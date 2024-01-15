from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializers


class ProductGet(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)
        return Response({'data': serializer.data})


class ProductPost(APIView):
    def post(self, request):
        serializers = ProductSerializers(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
        return Response({'data': serializers.data})


class ProductUpdate(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            meal = Product.objects.get(pk=pk)
        except:
            return Response('Meal is not Exist')
        serializers = ProductSerializers(data=request.data, instance=meal)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
        return Response({'data': serializers.data})

class ProductDelete(APIView):
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response("Not pk")

        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response("Product not found")

        product.delete()

        return Response("Продукт удален")