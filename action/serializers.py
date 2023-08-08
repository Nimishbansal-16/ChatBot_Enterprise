from rest_framework.serializers import ModelSerializer

from action.models import Action


class ActionSerializer(ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

    def create(self, validated_data):
        return Action.objects.create(**validated_data)
