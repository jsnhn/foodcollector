from django.contrib import admin
from .models import Food, Review, Ingredient, Photo

# Register your models here.
admin.site.register(Food)
admin.site.register(Review)
admin.site.register(Ingredient)
admin.site.register(Photo)
