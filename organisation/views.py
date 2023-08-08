from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError as DRFValidationError
from .models import Organisation
from .serializers import OrganisationSerializer


class OrganisationListCreateView(ListCreateAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    def post(self, request, *args, **kwargs):
        serializer = OrganisationSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except DRFValidationError as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class OrganisationRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = OrganisationSerializer(instance, data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except DRFValidationError as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)
