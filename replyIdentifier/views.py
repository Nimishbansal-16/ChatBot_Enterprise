from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from organisation.models import Organisation
from suggestion.models import Suggestions
from suggestion.serializers import SuggestionsSerializer
from .models import ReplyIdentifier
from .serializers import ReplyIdentifierSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_201_CREATED


class ReplyIdentifierListCreateView(ListCreateAPIView):
    queryset = ReplyIdentifier.objects.all()
    serializer_class = ReplyIdentifierSerializer

    def post(self, request, *args, **kwargs):
        # organisation_id = request.data.get('organisation')
        # suggestions = request.data.pop('suggestion', [])
        # for suggestion_id in suggestions:
        #     suggestion = get_object_or_404(Suggestions, id=suggestion_id)
        #     serializer.suggestions.add()

        # # this raises an exception
        # # Have to check ki if we don't find organisation then kya krna hai?
        # organisation = get_object_or_404(Organisation, id=organisation_id)
        serializer = ReplyIdentifierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ReplyIdentifierRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = ReplyIdentifier.objects.all()
    serializer_class = ReplyIdentifierSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ReplyIdentifierSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)
