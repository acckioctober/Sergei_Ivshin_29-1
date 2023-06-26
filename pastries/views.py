from django.shortcuts import render, get_object_or_404, redirect
from pastries.models import Cake, Taste, Filling, Topping, CakeType, Event
from pastries.forms import CakeCreateForm, EventCreateForm
from django.contrib.auth.decorators import login_required

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
                'user': request.user,
            })
        return render(request, "pastries/pastries.html", {'cakes_data': cakes_data})


def cake_detail(request, cake_id):
    if request.method == "GET":
        cake = get_object_or_404(Cake, id=cake_id)
        return render(request, 'pastries/cake_detail.html', {'cake': cake})


def specific_cakes_view(request):
    if request.method == "GET":
        cake_types = CakeType.objects.values_list('name', flat=True).distinct()
        specific_cake_types = CakeType.objects.filter(name__in=cake_types)
        context_data = {
            "specific_cake_types": specific_cake_types
        }
        return render(request, "pastries/specific_cake_types.html", context=context_data)


def specific_taste_view(request):
    if request.method == "GET":
        specific_tastes = Taste.objects.filter(available=True)
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

@login_required
def cake_create_view(request):
    if request.method == "GET":
        context_data = {
            "form": CakeCreateForm()
        }
        return render(request, "pastries/cake_create_form.html", context=context_data)

    if request.method == "POST":
        form = CakeCreateForm(request.POST, request.FILES)
        if form.is_valid():
            fillings = form.cleaned_data.pop('fillings')
            toppings = form.cleaned_data.pop('toppings')
            cake = Cake.objects.create(**form.cleaned_data)
            cake.fillings.set(fillings)
            cake.toppings.set(toppings)
            return redirect("/pastries/")
        return render(request, "pastries/cake_create_form.html", {"form": form})

@login_required
def list_event_view(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'pastries/events.html', {'events': events})

@login_required
def event_create_view(request):
    if request.method == "GET":
        context_data = {
            "form": EventCreateForm()
        }
        return render(request, "pastries/event_create_form.html", context=context_data)
    if request.method == 'POST':
        form = EventCreateForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            form.save_m2m()
            return redirect('/events/')
        return render(request, 'pastries/event_create_form.html', {'form': form})