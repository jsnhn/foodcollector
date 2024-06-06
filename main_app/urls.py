from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'), #route for the homepage
    path("about/", views.about, name="about"),
    path("foods/", views.foods_index, name='index'),
    path('foods/<int:food_id>/', views.foods_detail, name='detail'),
]