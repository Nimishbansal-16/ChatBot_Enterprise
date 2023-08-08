from rest_framework.serializers import ModelSerializer

from organisation.models import Organisation


class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = '__all__'

    def create(self, validated_data):
        return Organisation.objects.create(**validated_data)
