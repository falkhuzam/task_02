from django.shortcuts import render

def favourite_restaurants(request):
    return render(request, "pizza.html")