from django.db import models

from helper.models import BaseModel


# Create your models here.

class Organisation(BaseModel):
    name = models.CharField(max_length=256, blank=False)
    client_id = models.CharField(max_length=256, blank=False)
    api_key = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return 'Name: {}, Client ID: {}'.format(self.name, self.client_id)
