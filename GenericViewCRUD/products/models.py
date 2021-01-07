from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='product_photo/', blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)


@property
def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url