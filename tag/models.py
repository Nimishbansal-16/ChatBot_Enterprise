from django.db import models
from helper.models import BaseModel


# Create your models here.

class Tag(BaseModel):
    organisation = models.ForeignKey("organisation.Organisation", on_delete=models.CASCADE)
    intent = models.ForeignKey("intent.Intent", on_delete=models.CASCADE)
    subintent = models.ForeignKey("subintent.SubIntent", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=False)
