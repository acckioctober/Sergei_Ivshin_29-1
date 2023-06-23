from django.contrib import admin
from pastries.models import Cake, Taste, Filling, Topping, CakeType
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple


admin.site.register(CakeType)
admin.site.register(Taste)
admin.site.register(Filling)
admin.site.register(Topping)



class CakeAdminForm(forms.ModelForm):
    fillings = forms.ModelMultipleChoiceField(
        queryset=Filling.objects.all(),
        widget=FilteredSelectMultiple("Fillings", is_stacked=False),
        required=False
    )

    toppings = forms.ModelMultipleChoiceField(
        queryset=Topping.objects.all(),
        widget=FilteredSelectMultiple("Toppings", is_stacked=False),
        required=False
    )

    class Meta:
        model = Cake
        fields = "__all__"


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    form = CakeAdminForm