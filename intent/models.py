from django.db import models

from helper.models import BaseModel


# Create your models here.

class Intent(BaseModel):
    organisation = models.ForeignKey("organisation.Organisation", on_delete=models.CASCADE)
    products = models.ForeignKey("product.Products", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return 'Name: {}, Product : {}, Organisation: {}'.format(
            self.name, self.products, self.organisation)
