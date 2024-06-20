from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Food, Ingredient, Photo
from .forms import ReviewForm
import uuid
import boto3
import os
import requests


# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    response = requests.get('https://foodish-api.com/api/')
    food_img = response.json().get('image') #fact or the none value because we are using get. if we use bracket it could display error
    return render(request, "about.html", {'image': food_img})

def foods_index(request):
    foods = Food.objects.all()
    return render(request, 'foods/index.html', {
        'foods': foods
    })

def foods_detail(request, food_id):
    food = Food.objects.get(id=food_id)
    id_list = food.ingredients.all().values_list('id')
    ingredient_food_doesnt_have = Ingredient.objects.exclude(id__in=id_list)
    review_form = ReviewForm()
    return render(request, 'foods/detail.html', {
        'food': food,
        'review_form': review_form,
        'ingredients': ingredient_food_doesnt_have
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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

def assoc_ingredient(request, food_id, ingredient_id):
    Food.objects.get(id=food_id).ingredients.add(ingredient_id)
    return redirect('detail', food_id=food_id)

def unassoc_ingredient(request, food_id, ingredient_id):
    Food.objects.get(id=food_id).ingredients.remove(ingredient_id)
    return redirect('detail', food_id=food_id)

def add_photo(request, food_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, food_id=food_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', food_id=food_id)