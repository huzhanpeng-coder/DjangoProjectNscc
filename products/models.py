from django.db import models
from categories import models as category_models

# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(category_models.Category, default=None, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=100)
    quantity = models.IntegerField()
    sku = models.IntegerField()
    picture = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title
# Create your models here.
    