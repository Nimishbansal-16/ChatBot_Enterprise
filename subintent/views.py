from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from intent.models import Intent
from organisation.models import Organisation
from product.models import Products
from .models import SubIntent
from .serializers import SubIntentSerializer
from django.shortcuts import get_object_or_404


class SubIntentListCreateView(ListCreateAPIView):
    queryset = SubIntent.objects.all()
    serializer_class = SubIntentSerializer

    def post(self, request, *args, **kwargs):
        # intent_id = request.data.get('intent')
        # organisation_id = request.data.get('organisation')
        # product_id = request.data.get('product')
        # # Have to check ki if we dont find intent then kya krna hai?
        # intent = get_object_or_404(Intent, id=intent_id)
        # organisation = get_object_or_404(Organisation, id=organisation_id)
        # product = get_object_or_404(Products, id=product_id)

        serializer = SubIntentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SubIntentRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = SubIntent.objects.all()
    serializer_class = SubIntentSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SubIntentSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)
