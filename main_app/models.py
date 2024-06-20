from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredients_detail', kwargs={'pk': self.id})
    
class Food(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    vegetarian = models.BooleanField(default=False)
    ingredients = models.ManyToManyField(Ingredient)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'food_id': self.id})
        # Think of the reverse() function as the code equivalent to the url template tag. It returns the correct path for the detail

    def review_for_today(self):
        return self.review_set.filter(date=date.today()).count() >= self.review_set.all().count()

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

class Photo(models.Model):
    url = models.CharField(max_length=200)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for food_id: {self.food_id} @{self.url}"