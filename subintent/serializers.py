from rest_framework.serializers import ModelSerializer

from subintent.models import SubIntent


class SubIntentSerializer(ModelSerializer):
    class Meta:
        model = SubIntent
        fields = '__all__'

    def create(self, validated_data):
        return SubIntent.objects.create(**validated_data)
