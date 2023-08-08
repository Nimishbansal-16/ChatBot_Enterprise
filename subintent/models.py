from django.db import models

from helper.models import BaseModel


# Create your models here.

class SubIntent(BaseModel):
    intent = models.ForeignKey("intent.Intent", on_delete=models.CASCADE)
    organisation = models.ForeignKey("organisation.Organisation", on_delete=models.CASCADE)
    products = models.ForeignKey("product.Products", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return 'Name: {}, Product: {}, Organisation: {}, Intent: {}'.format(
            self.name, self.products, self.organisation, self.intent)
