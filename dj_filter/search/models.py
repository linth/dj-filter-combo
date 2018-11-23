from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    description = models.TextField()
    release_date = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
