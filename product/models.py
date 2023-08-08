from django.db import models

from helper.models import BaseModel


# Create your models here.

class Products(BaseModel):
    organisation = models.ForeignKey("organisation.Organisation", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return 'Name: {}, Organisation: {}'.format(
            self.name, self.organisation)
