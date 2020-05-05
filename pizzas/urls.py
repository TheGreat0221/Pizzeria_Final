from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'), ## home page
    path('pizzas', views.pizzas, name='pizzas'), ## pizza page
    path('pizzas/<int:pizza_id>/', views.pizza,name="pizza"), ## drill down into each pizza to see toppings
    
    path('comment/<int:pizza_id>/', views.comment, name='comment'), ## comment under pizza
    path('edit_comment/<int:commend_id>/', views.edit_comment, name='edit_comment'), ## edit comments
]