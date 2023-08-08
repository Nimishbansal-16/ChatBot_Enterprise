from django.db import models

from helper.models import BaseModel


# Create your models here.
class Action(BaseModel):
    name = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return 'Name: {}'.format(
            self.name)
