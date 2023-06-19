from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from pastries.models import Cake

# def hello(request):
#     if request.method == "GET":
#         return HttpResponse("Hello! It's my pastries project")
#
#
# def now_date(request):
#     if request.method == "GET":
#         now = datetime.now()
#         return HttpResponse("Current date and time: " + now.strftime("%Y-%m-%d %H:%M:%S"))
#
#
# def goodbye(request):
#     if request.method == "GET":
#         return HttpResponse("Goodbye dear user!")

def main_page(request):
    if request.method == "GET":
        return render(request, "layouts/index.html")

# def pastries_view(request):
#     if request.method == "GET":
#         cakes = Cake.objects.all()
#         context_data = {
#             "cakes": cakes
#         }
#         return render(request, "pastries/pastries.html", context=context_data)


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