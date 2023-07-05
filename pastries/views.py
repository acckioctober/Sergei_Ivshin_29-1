from django.shortcuts import render
from pastries.models import Cake, Taste, Filling, Topping, CakeType, Event
from pastries.forms import CakeCreateForm, EventCreateForm
from django.db.models import Q
from django.db.models.functions import Lower
from pastries.constants import PAGINATION_LIMIT
import math

from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



class MainPageCBV(ListView):
    model = Cake
    template_name = "layouts/index.html"


class PastriesCBV(ListView):
    model = Cake
    template_name = "pastries/pastries.html"
    def get(self, request, *args, **kwargs):
        cakes = self.model.objects.all()
        search_query = request.GET.get('q', '')  # Получаем поисковый запрос, если он есть, иначе - пустая строка
        if search_query:
            cakes = cakes.annotate(
                lower_cake_type_name=Lower('cake_type__name'),
                lower_cake_type_description=Lower('cake_type__description'),
                lower_taste_name=Lower('taste__name'),
                lower_taste_description=Lower('taste__description'),
            ).filter(
                Q(lower_cake_type_name__contains=search_query.lower()) |
                Q(lower_cake_type_description__contains=search_query.lower()) |
                Q(lower_taste_name__contains=search_query.lower()) |
                Q(lower_taste_description__contains=search_query.lower())
            ).distinct()
        page = int(request.GET.get('page', 1))
        max_page = math.ceil(cakes.count() / PAGINATION_LIMIT)
        cakes = cakes[(page - 1) * PAGINATION_LIMIT:page * PAGINATION_LIMIT]
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
        pages = range(1, max_page + 1)
        return render(request, self.template_name, {'cakes_data': cakes_data, 'pages': pages})


class CakeDetailCBV(DetailView):
    model = Cake
    template_name = "pastries/cake_detail.html"
    context_object_name = "cake"
    pk_url_kwarg = "cake_id"


class SpecificCakesCBV(ListView):
    # Просмотр списка тортов по конкретным типам
    model = CakeType
    template_name = "pastries/specific_cake_types.html"
    context_object_name = "specific_cake_types"


class SpecificTasteCBV(ListView):
    # Просмотр списка тортов по конкретным вкусам
    model = Taste
    template_name = "pastries/specific_tastes.html"
    context_object_name = "specific_tastes"


class SpecificToppingCBV(ListView):
    # Просмотр списка тортов по конкретным начинкам
    model = Topping
    template_name = "pastries/specific_toppings.html"
    context_object_name = "specific_toppings"


class SpecificFillingCBV(ListView):
    # Просмотр списка тортов по конкретным начинкам
    model = Filling
    template_name = "pastries/specific_fillings.html"
    context_object_name = "specific_fillings"


class CakeCreateCBV(LoginRequiredMixin, CreateView):
    # Создание торта
    model = Cake
    form_class = CakeCreateForm
    template_name = "pastries/cake_create_form.html"
    success_url = reverse_lazy("pastries")


class EventListCBV(LoginRequiredMixin, ListView):
    # Список событий пользователя
    model = Event
    template_name = 'pastries/events.html'
    context_object_name = 'events'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class EventCreateCBV(LoginRequiredMixin, CreateView):
    # Создание события для пользователя
    model = Event
    form_class = EventCreateForm
    template_name = "pastries/event_create_form.html"
    success_url = reverse_lazy("events")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)