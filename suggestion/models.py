from django.db import models

from helper.models import BaseModel


# Create your models here.
class Suggestions(BaseModel):
    name = models.CharField(max_length=255, blank=False)
    content = models.JSONField(default=dict, help_text='{"language": "en", "content_data": "Some content"}')
    count = models.PositiveIntegerField(default=0)
    organisation = models.ForeignKey("organisation.Organisation", on_delete=models.CASCADE)
    action = models.ForeignKey("action.Action", on_delete=models.CASCADE)

    def __str__(self):
        return 'Name: {}, Content : {}, Count: {}, Organisation: {}, Action: {}, '.format(
            self.name, self.content, self.count, self.organisation, self.action)
