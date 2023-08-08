from rest_framework.serializers import ModelSerializer, ValidationError
from rest_framework.generics import get_object_or_404

from replyIdentifier.models import ReplyIdentifier
from suggestion.models import Suggestions


def validate_content(value):
    if not isinstance(value, dict) or 'language' not in value or 'content_data' not in value:
        raise ValidationError(
            "Invalid content format. The content must be a JSON object with 'language' and 'content_data' keys.")
    return value


class ReplyIdentifierSerializer(ModelSerializer):
    # suggestions = SuggestionsSerializer(many=True)  # Use the SuggestionsSerializer for the suggestions field
    # suggestions = PrimaryKeyRelatedField(queryset=Suggestions.objects.all(), many=True)

    class Meta:
        model = ReplyIdentifier
        fields = '__all__'
        extra_kwargs = {
            'content': {'validators': [validate_content]},
        }

    def create(self, validated_data):
        suggestions_data = validated_data.pop('suggestions', [])
        reply_identifier = ReplyIdentifier.objects.create(**validated_data)
        # for suggestion_data in suggestions_data:
        # suggestion, _ = get_object_or_404(Suggestions, id=suggestion_data)
        #     reply_identifier.suggestions.add(suggestion_data)
        # suggestion_id.append(suggestion_data)
        reply_identifier.suggestions.set(suggestions_data)
        return reply_identifier
        # return ReplyIdentifier.objects.create(**validated_data)

    def update(self, instance, validated_data):
        suggestions_data = validated_data.pop('suggestions', [])
        instance = super().update(instance, validated_data)

        instance.suggestions.clear()
        # for suggestion_data in suggestions_data:
        #     suggestion, _ = Suggestions.objects.get_or_create(**suggestion_data)
        #     instance.suggestions.add(suggestion)
        instance.suggestions.set(suggestions_data)
        return instance
