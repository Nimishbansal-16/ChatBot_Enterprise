from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_201_CREATED
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from action.models import Action
from organisation.models import Organisation
from .models import Suggestions
from .serializers import SuggestionsSerializer
from django.shortcuts import get_object_or_404


class SuggestionsListCreateView(ListCreateAPIView):
    queryset = Suggestions.objects.all()
    serializer_class = SuggestionsSerializer

    def post(self, request, *args, **kwargs):
        # organisation_id = request.data.get('organisation')
        # action_id = request.data.get('action')
        # # this raises an exception
        # # Have to check ki if we don't find organisation then kya krna hai?
        # organisation = get_object_or_404(Organisation, id=organisation_id)
        # action = get_object_or_404(Action, id=action_id)
        serializer = SuggestionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SuggestionsRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Suggestions.objects.all()
    serializer_class = SuggestionsSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = SuggestionsSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)
