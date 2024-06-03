from django.shortcuts import render

foods = [
  {'name': 'Mcdonalds', 'meals': 'Big Mac', 'review': 'Very average', 'rating': 5},
  {'name': 'In n Out', 'meals': 'Double Double', 'review': 'Super tasty', 'rating': 10},
]

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def foods_index(request):
    return render(request, 'foods/index.html', {
        'foods': foods
    })