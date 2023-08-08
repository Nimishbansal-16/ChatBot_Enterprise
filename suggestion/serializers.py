from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Suggestions


def validate_content(value):
    if not isinstance(value, dict) or 'language' not in value or 'content_data' not in value:
        raise ValidationError(
            "Invalid content format. The content must be a JSON object with 'language' and 'content_data' keys.")
    return value


class SuggestionsSerializer(ModelSerializer):
    class Meta:
        model = Suggestions
        fields = '__all__'
        extra_kwargs = {
            'content': {'validators': [validate_content]},
        }

    # This did not work
    # def validate(self, data):
    #     value = data['content']
    #     # Check if the value is a dictionary and contains the required keys
    #     if not isinstance(value, dict) or 'language' not in value or 'content_data' not in value:
    #         raise ValidationError(
    #             "Invalid content format. The content must be a JSON object with 'language' and 'content_value' keys.")
    #     return value

    def create(self, validated_data):
        return Suggestions.objects.create(**validated_data)
