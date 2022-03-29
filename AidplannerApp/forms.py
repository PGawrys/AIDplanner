from django import forms
# from django.core.exceptions import ValidationError
from AidplannerApp.models import Item, Service, Spot


class AddItemForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea())
    description = forms.CharField(widget=forms.Textarea())
    number_needed = forms.IntegerField()
    number_delivered = forms.IntegerField()


class AddServiceForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea())
    description = forms.CharField(widget=forms.Textarea())
    people_needed = forms.IntegerField()
    hours_needed = forms.IntegerField()
    spot = forms.ModelChoiceField(queryset=Spot.objects.all())


class AddSpotForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea())
    address = forms.CharField(widget=forms.Textarea())
    details = forms.CharField(widget=forms.Textarea())


class AddItemModelForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


class AddServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

