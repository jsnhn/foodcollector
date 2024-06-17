from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Food, Ingredient
from .forms import ReviewForm


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
    review_form = ReviewForm
    return render(request, 'foods/detail.html', {
        'food': food,
        'review_form': review_form
    })

def add_review(request, food_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.food_id = food_id
        new_review.save()
    return redirect('detail', food_id=food_id)

class FoodCreate(CreateView):
    model = Food
    fields = ['name', 'cuisine']
    # success_url = '/foods/{id}'

class FoodUpdate(UpdateView):
    model = Food
    fields = ['cuisine', 'review', 'rating', 'vegetarian']

class FoodDelete(DeleteView):
    model = Food
    success_url = '/foods'

class IngredientList(ListView):
    model = Ingredient

class IngredientDetail(DetailView):
    model = Ingredient

class IngredientCreate(CreateView):
    model = Ingredient
    fields = '__all__'

class IngredientUpdate(UpdateView):
    model = Ingredient
    fields = ['name']

class IngredientDelete(DeleteView):
    model = Ingredient
    success_url = '/ingredients'