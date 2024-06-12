from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'food_id': self.id})
        # Think of the reverse() function as the code equivalent to the url template tag. It returns the correct path for the detail

class Review(models.Model):
    date = models.DateField()
    text = models.CharField(max_length=500)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ]
    ) 

    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rating} on {self.date}"
    
    class Meta:
        ordering = ['-date']