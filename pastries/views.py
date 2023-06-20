from django.shortcuts import render, get_object_or_404
from pastries.models import Cake, Taste, Filling, Topping


def main_page(request):
    if request.method == "GET":
        return render(request, "layouts/index.html")


def pastries_view(request):
    if request.method == "GET":
        cakes = Cake.objects.all()
        cakes_data = []
        for cake in cakes:
            fillings = ", ".join([filling.name for filling in cake.fillings.all()])
            toppings = ", ".join([topping.name for topping in cake.toppings.all()])
            cakes_data.append({
                'cake': cake,
                'fillings': fillings,
                'toppings': toppings,
            })
        return render(request, "pastries/pastries.html", {'cakes_data': cakes_data})


def cake_detail(request, cake_id):
    if request.method == "GET":
        cake = get_object_or_404(Cake, id=cake_id)
        return render(request, 'pastries/cake_detail.html', {'cake': cake})


def specific_cakes_view(request):
    if request.method == "GET":
        cake_names = Cake.objects.values_list('name', flat=True).distinct()
        specific_cakes = Cake.objects.filter(name__in=cake_names)
        context_data = {
            "specific_cakes": specific_cakes
        }
        return render(request, "pastries/specific_cakes.html", context=context_data)


def specific_taste_view(request):
    if request.method == "GET":
        taste_names = Taste.objects.values_list('name', flat=True).distinct()
        specific_tastes = Taste.objects.filter(name__in=taste_names)
        context_data = {
            "specific_tastes": specific_tastes
        }
        return render(request, "pastries/specific_tastes.html", context=context_data)

def specific_filling_view(request):
    if request.method == "GET":
        filling_names = Filling.objects.values_list('name', flat=True).distinct()
        specific_fillings = Filling.objects.filter(name__in=filling_names)
        context_data = {
            "specific_fillings": specific_fillings
        }
        return render(request, "pastries/specific_fillings.html", context=context_data)

def specific_topping_view(request):
    if request.method == "GET":
        topping_names = Topping.objects.values_list('name', flat=True).distinct()
        specific_toppings = Topping.objects.filter(name__in=topping_names)
        context_data = {
            "specific_toppings": specific_toppings
        }
        return render(request, "pastries/specific_toppings.html", context=context_data)