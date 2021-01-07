from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300, default='', null=True, blank=True)
    price = models.IntegerField(default=0)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.title
