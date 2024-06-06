from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    review = models.TextField(max_length=250)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    vegitarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name