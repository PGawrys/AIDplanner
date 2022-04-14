from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.utils import timezone
from django.views import View


from AidplannerApp.forms import AddItemModelForm, AddSpotForm, AddServiceModelForm, \
    AddItemCollectionForm, AddServiceCollectionForm, EditItemInCollectionForm, EditServiceInCollectionForm
from AidplannerApp.models import Spot, Service, Item, ServiceCollection, ItemCollection, ItemCollectionItems, \
    ServiceCollectionServices


class IndexView(View):
    """Widok głównej strony."""
    def get(self, request):
        return render(request, 'base.html', {'date':timezone.now()})


class AddSpot(LoginRequiredMixin, View):
    """Widok umożliwiający dodanie nowej lokalizacji."""
    def get(self, request):
        return render(request, 'manual_form.html')

    def post(self, request):
        name = request.POST['name']
        address = request.POST['address']
        details = request.POST['details']
        Spot.objects.create(name=name, address=address, details=details)
        return redirect('add_spot')


class ShowItem(View):
    """Widok listy istniejących przedmiotów wraz z formularzem do ich dodawania."""
    def get(self, request):
        return render(request, 'list.html', {'object_list': Item.objects.all()})


class ShowService(View):
    """Widok listy istniejących usług wraz z formularzem do ich dodawania."""
    def get(self, request):
        return render(request, 'list.html', {'object_list': Service.objects.all()})


class ShowSpot(View):
    """Widok listy istniejących lokalizacji."""
    def get(self, request):
        return render(request, 'list.html', {'object_list': Spot.objects.all(), 'spot': 'spot'})


class ShowStatsView(View):
    """Widok statystyk."""
    def get(self, request):
        return render(request, 'stats.html')


class ShowScheduleView(View):
    """Widok tablicy zbiórek."""
    def get(self, request):
        return render(request, 'schedule.html')


class ShowDetailSpot(View):
    """Widok pokazujący szczegóły lokacji."""
    def get(self, request, id):
        form = AddItemModelForm()
        spot = Spot.objects.get(pk=id)
        return render(request, "spot_detail.html", {'spot': spot, 'form': form})

    def post(self, request, id):
        spot = Spot.objects.get(pk=id)
        form = AddItemModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.spot = spot
            post.save()
            return redirect(f'/spot/{spot.id}/')
        return render(request, 'form.html', {'form': form})


class UpdateItemView(View):
    """Widok do edycji istniejącego przedmiotu."""
    def get(self, request, id):
        item = Item.objects.get(pk=id)
        form = AddItemModelForm(instance=item)
        return render(request, 'form2.html', {'form':form})

    def post(self, request, id):
        item = Item.objects.get(pk=id)
        form = AddItemModelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        return render(request, 'form2.html', {'form': form})


class UpdateServiceView(View):
    """Widok do edycji istniejącej usługi."""
    def get(self, request, id):
        service = Service.objects.get(pk=id)
        form = AddServiceModelForm(instance=service)
        return render(request, 'form2.html', {'form':form})

    def post(self, request, id):
        service = Service.objects.get(pk=id)
        form = AddServiceModelForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
        return render(request, 'form2.html', {'form': form})


class DeleteItemView(View):
    """Widok usuwający przedmiot z listy."""
    def get(self, request, id):
        return render(request, 'form2.html', {})

    def post(self, request, id):
        item = Item.objects.get(pk=id)
        item.delete()
        return redirect('item_list')


class DeleteServiceView(View):
    """Widok usuwający usługę z listy."""
    def get(self, request, id):
        return render(request, 'form2.html', {})

    def post(self, request, id):
        service = Service.objects.get(pk=id)
        service.delete()
        return redirect('service_list')


class ShowCollectionsView(View):
    """Widok istniejących zbiórek"""
    def get(self, request):
        itemlist = ItemCollection.objects.all()
        servicelist = ServiceCollection.objects.all()
        return render(request, 'collectionsEXTEN.html', {'date': timezone.now(), "itemcollections": itemlist, "servicecollections": servicelist})


class ShowDetailItemList(View):
    """Widok listy dodanych przedmiotów, z których można korzystać przy dodawaniu zbiórek."""
    def get(self, request):
        form = AddItemModelForm()
        itemlist = Item.objects.all()
        return render(request, 'item_list.html', {'itemlist': itemlist, 'form': form})

    def post(self, request):
        form = AddItemModelForm(request.POST)
        itemlist = Item.objects.all()
        if form.is_valid():
            item = form.save()
            item.save()
            return redirect('item_list')
        return render(request, 'item_list.html', {'itemlist': itemlist, 'form': form})


class ShowDetailServiceList(View):
    """Widok listy dodanych usług, z których można korzystać przy dodawaniu zbiórek."""
    def get(self, request):
        form = AddServiceModelForm()
        servicelist = Service.objects.all()
        return render(request, 'service_list.html', {'servicelist': servicelist, 'form': form})

    def post(self, request):
        form = AddServiceModelForm(request.POST)
        servicelist = Service.objects.all()
        if form.is_valid():
            service = form.save()
            service.save()
            return redirect('service_list')
        return render(request, 'service_list.html', {'servicelist': servicelist, 'form': form})


class AddCollectionItem(LoginRequiredMixin, View):
    """Widok dodający nową zbiórkę przedmiotów. Usługi wybiera się sposród wczesniej dodanych, istniejących przedmiotów (model Item)"""
    def get(self, request):
        form = AddItemCollectionForm()
        items = Item.objects.all()
        return render(request, 'form2.html', {'form': form, 'items': items})

    def post(self, request):
        form = AddItemCollectionForm(request.POST)
        items = Item.objects.all()
        if form.is_valid():
            collectionitem = form.save()
            items = request.POST.getlist('items')
            for item_id in items:
                if Item.objects.all().exists():
                    item = Item.objects.get(id=item_id)
                    collectionitem.items.add(item)
            collectionitem.save()
            return redirect('add_collection_item')
        return render(request, 'form2.html', {'form': form, 'items': items})


class AddCollectionService(LoginRequiredMixin, View):
    """Widok dodający nową zbiórkę usług. Usługi wybiera się sposród wczesniej dodanych, istniejących usług (model Service)"""
    def get(self, request):
        form = AddServiceCollectionForm()
        services = Service.objects.all()
        return render(request, 'form2.html', {'form': form, 'services': services})

    def post(self, request):
        form = AddServiceCollectionForm(request.POST)
        services = Service.objects.all()
        if form.is_valid():
            collectionservice = form.save()
            for service in services:
                if Service.objects.all().exists():
                    service = Service.objects.get(id=service.id)
                    collectionservice.services.add(service)
            collectionservice.save()
            return redirect('add_collection_service')

        return render(request, 'form2.html', {'form': form, 'services': services})


class UpdateItemCollectionView(LoginRequiredMixin, View):
    """Widok otwierający formularz, tak jak przy tworzeniu nowej zbiórki przedmiotów, pozwalający edytować istniejące już instancje zbiórek przedmiotów."""

    def get(self, request, id):
        itemcollection = ItemCollection.objects.get(pk=id)
        form = AddItemCollectionForm(instance=itemcollection)
        return render(request, 'edit_item_collection.html', {'form':form, 'itemcollection':itemcollection})

    def post(self, request, id):
        itemcollection = ItemCollection.objects.get(pk=id)
        form = AddItemCollectionForm(request.POST, instance=itemcollection)
        if form.is_valid():
            form.save()
            return redirect('collections')
        return render(request, 'edit_item_collection.html', {'form':form, 'itemcollection':itemcollection})


class DeleteItemCollectionView(LoginRequiredMixin, View):
    """Widok do usuwania zbiórek przedmiotów."""
    def get(self, request, id):
        return render(request, 'form2.html', {})

    def post(self, request, id):
        itemcollection = ItemCollection.objects.get(pk=id)
        itemcollection.delete()
        return redirect('collections')


class UpdateServiceCollectionView(LoginRequiredMixin, View):
    """Widok otwierający formularz, tak jak przy tworzeniu nowej zbiórki usług, pozwalający edytować istniejące już instancje zbiórek usług."""
    def get(self, request, id):
        servicecollection = ServiceCollection.objects.get(pk=id)
        form = AddServiceCollectionForm(instance=servicecollection)
        return render(request, 'edit_service_collection.html', {'form':form, 'servicecollection': servicecollection})

    def post(self, request, id):
        servicecollection = ServiceCollection.objects.get(pk=id)
        form = AddServiceCollectionForm(request.POST, instance=servicecollection)
        if form.is_valid():
            form.save()
            return redirect('collections')
        return render(request, 'edit_service_collection.html', {'form':form, 'servicecollection': servicecollection})


class DeleteServiceCollectionView(LoginRequiredMixin, View):
    """Widok do usuwania zbiórek usług."""
    def get(self, request, id):
        return render(request, 'form2.html', {})

    def post(self, request, id):
        servicecollection = ServiceCollection.objects.get(pk=id)
        servicecollection.delete()
        return redirect('collections')


class UpdateSpotView(LoginRequiredMixin, View):
    """Widok do edytowania lokalizacji."""
    def get(self, request, id):
        spot = Spot.objects.get(pk=id)
        form = AddSpotForm(instance=spot)
        return render(request, 'form2.html', {'form': form})

    def post(self, request, id):
        spot = Spot.objects.get(pk=id)
        form = AddSpotForm(request.POST, instance=spot)
        if form.is_valid():
            form.save()
            return redirect('show_spot')
        return render(request, 'form2.html', {'form': form})


class DeleteSpotView(LoginRequiredMixin, View):
    """Widok do usuwania lokalizacji."""
    def get(self, request, id):
        return render(request, 'form2.html', {})

    def post(self, request, id):
        spot = Spot.objects.get(pk=id)
        spot.delete()
        return redirect('show_spot')


class UpdateItemInCollectionView(LoginRequiredMixin, View):
    def get(self, request, id):
        item = ItemCollectionItems.objects.get(id=id)
        form = EditItemInCollectionForm(instance=item)
        return render(request, 'form2.html', {'form': form, 'item': item})

    def post(self, request, id):
        item = ItemCollectionItems.objects.get(id=id)
        form = EditItemInCollectionForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('collections')
        return render(request, 'form2.html', {'form': form, 'item': item})


class UpdateServiceInCollectionView(LoginRequiredMixin, View):
    def get(self, request, id):
        service = ServiceCollectionServices.objects.get(id=id)
        form = EditServiceInCollectionForm(instance=service)
        return render(request, 'form2.html', {'form': form, 'service': service})

    def post(self, request, id):
        service = ServiceCollectionServices.objects.get(id=id)
        form = EditServiceInCollectionForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('collections')
        return render(request, 'form2.html', {'form': form, 'service': service})