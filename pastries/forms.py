from django import forms
from pastries.models import Cake, Taste, Filling, Topping, CakeType, Event


class CakeCreateForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['cake_type', 'taste', 'fillings', 'toppings', 'weight', 'image', 'add_info']
    cake_type = forms.ModelChoiceField(queryset=CakeType.objects.filter(available=True), empty_label='Выберите вид торта')
    taste = forms.ModelChoiceField(queryset=Taste.objects.filter(available=True), empty_label='Выберите вкус')
    fillings = forms.ModelMultipleChoiceField(queryset=Filling.objects.filter(available=True), widget=forms.CheckboxSelectMultiple)
    toppings = forms.ModelMultipleChoiceField(queryset=Topping.objects.filter(available=True), widget=forms.CheckboxSelectMultiple)
    weight = forms.DecimalField(max_digits=4, decimal_places=2)
    image = forms.FileField(required=False)
    add_info = forms.CharField(widget=forms.Textarea, required=False)


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'cakes']
        widgets = {
            'cakes': forms.CheckboxSelectMultiple
        }