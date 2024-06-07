from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Food


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def foods_index(request):
    foods = Food.objects.all()
    return render(request, 'foods/index.html', {
        'foods': foods
    })

def foods_detail(request, food_id):
    food = Food.objects.get(id=food_id)
    return render(request, 'foods/detail.html', {
        'food': food
    })

class FoodCreate(CreateView):
    model = Food
    fields = ['name', 'cuisine', 'review', 'rating']
    success_url = '/foods/{id}'