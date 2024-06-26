from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'), #route for the homepage
    path("about/", views.about, name="about"),
    path("foods/", views.foods_index, name='index'),
    path('foods/<int:food_id>/', views.foods_detail, name='detail'),
    path('foods/create/', views.FoodCreate.as_view(), name='foods_create'),
    path('foods/<int:pk>/update/', views.FoodUpdate.as_view(), name='foods_update'),
    path('foods/<int:pk>/delete.', views.FoodDelete.as_view(), name='foods_delete'),
    path('foods/<int:food_id>/add_review/', views.add_review, name='add_review'),
    path('foods/<int:food_id>/add_photo/', views.add_photo, name='add_photo'),
    path('foods/<int:food_id>/assoc_ingredient/<int:ingredient_id>/', views.assoc_ingredient, name='assoc_ingredient'),
    path('foods/<int:food_id>/unassoc_ingredient/<int:ingredient_id>/', views.unassoc_ingredient, name='unassoc_ingredient'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredients_index'),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view(), name='ingredients_detail'),
    path('ingredients/create/', views.IngredientCreate.as_view(), name='ingredients_create'),
    path('ingredients/<int:pk>/update/', views.IngredientUpdate.as_view(), name='ingredients_update'),
    path('ingredients/<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredients_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]

