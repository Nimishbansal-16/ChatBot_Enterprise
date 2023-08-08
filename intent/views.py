from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_201_CREATED
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from organisation.models import Organisation
from product.models import Products
from .models import Intent
from .serializers import IntentSerializer
from django.shortcuts import get_object_or_404


class IntentListCreateView(ListCreateAPIView):
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer

    def post(self, request, *args, **kwargs):
        # organisation_uuid = request.data.get('organisation')
        # product__uuid = request.data.get('product')
        # # this raises an exception
        # # Have to check ki if we don't find organisation then kya krna hai?
        # organisation = get_object_or_404(Organisation, id=organisation_uuid)
        # product = get_object_or_404(Products, id=product__uuid)
        serializer = IntentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class IntentRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Intent.objects.all()
    serializer_class = IntentSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = IntentSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)
