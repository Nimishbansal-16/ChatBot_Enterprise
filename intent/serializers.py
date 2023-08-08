from rest_framework.serializers import ModelSerializer

from intent.models import Intent


class IntentSerializer(ModelSerializer):
    class Meta:
        model = Intent
        fields = '__all__'

    def create(self, validated_data):
        return Intent.objects.create(**validated_data)
