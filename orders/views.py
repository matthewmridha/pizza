from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu, Topping
# Create your views here.
def index(request):
    pizza_regular = Menu.objects.all().filter(catagory="Pizza Regular")
    pizza_sicilian = Menu.objects.all().filter(catagory="Pizza Sicilian")
    subs = Menu.objects.all().filter(catagory="Sub")
    pasta = Menu.objects.all().filter(catagory="Pasta")
    salad = Menu.objects.all().filter(catagory="Salad")
    dinner_plate = Menu.objects.all().filter(catagory="Dinner Plate")
    toppings = Topping.objects.all()
    context = {
        "pizza_regular" : pizza_regular,
        "pizza_sicilian" : pizza_sicilian,
        "subs" : subs,
        "pasta" : pasta,
        "salad" : salad,
        "dinner_plate" : dinner_plate,
        "toppings" : toppings,
        "empty" : "not available at the moment"
    }
    return render(request, "menu.html", context)
