from enum import Enum

from django.db import models

from helper.models import BaseModel


# Create your models here.
class ReplyIdentifier(BaseModel):

    class TypeChoices(Enum):
        WIDGET = 'Widget'
        TEXT = 'Text'

    name = models.CharField(max_length=256, blank=False)
    organisation = models.ForeignKey("organisation.Organisation", on_delete=models.CASCADE)
    content = models.JSONField(default=dict, help_text='{"language": "en", "content_data": "Some content"}',
                               blank=True)
    type = models.CharField(max_length=10, choices=[(choice.value, choice.name) for choice in TypeChoices])
    input_allowed = models.BooleanField(default=False)
    content_url = models.URLField(max_length=256, blank=True, null=True)
    suggestions = models.ManyToManyField("suggestion.Suggestions", blank=True)

    def __str__(self):
        return 'Name: {}, Organisation : {}, Content : {}, type : {}, Content URL: {}, Suggestions: {} '.format(
            self.name, self.organisation, self.content, self.type, self.content_url, self.suggestions)
