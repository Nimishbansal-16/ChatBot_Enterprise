from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError as DRFValidationError
from .models import Action
from .serializers import ActionSerializer


class ActionListCreateView(ListCreateAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

    def post(self, request, *args, **kwargs):
        serializer = ActionSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except DRFValidationError as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)


class ActionRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ActionSerializer(instance, data=request.data)
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
