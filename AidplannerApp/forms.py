from django import forms
from AidplannerApp.models import Item, Service, Spot, ItemCollection, ServiceCollection, ItemCollectionItems, \
    ServiceCollectionServices


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


class AddSpotForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea())
    address = forms.CharField(widget=forms.Textarea())
    details = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Spot
        fields = '__all__'


class AddItemCollectionForm(forms.ModelForm):

    class Meta:
        model = ItemCollection
        exclude = ['items']


class AddServiceCollectionForm(forms.ModelForm):

    class Meta:
        model = ServiceCollection
        exclude = ['services']


class AddItemModelForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'


class AddServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class EditItemInCollectionForm(forms.ModelForm):
    class Meta:
        model = ItemCollectionItems
        fields = ['number_needed', 'number_delivered']


class EditServiceInCollectionForm(forms.ModelForm):
    class Meta:
        model = ServiceCollectionServices
        fields = ['hours_needed', 'people_needed']


