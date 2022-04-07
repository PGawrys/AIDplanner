from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView

from AidplannerApp.forms import AddItemForm, AddItemModelForm, AddSpotForm, AddServiceForm, AddServiceModelForm
from AidplannerApp.models import Spot, Service, Item, ServiceList, ItemList


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html', {'date':"DATE"})


class IndexView2(View):

    def get(self, request):
        return render(request, 'secondaryIndex.html')


class AddSpot(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'manual_form.html')

    def post(self, request):
        name = request.POST['name']
        address = request.POST['address']
        details = request.POST['details']
        Spot.objects.create(name=name, address=address, details=details)
        return redirect('add_spot')


class AddItemView(View):

    def get(self, request):
        form = AddItemForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            number_needed = form.cleaned_data['number_needed']
            number_delivered = form.cleaned_data['number_delivered']
            Item.objects.create(name=name, description=description, number_needed=number_needed, number_delivered=number_delivered)
            return redirect('add_item')
        return render(request, 'form.html', {'form': form})


class AddServiceView(View):     #dawny addPOSTview

    def get(self, request):
        form = AddServiceForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddServiceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            hours_needed = form.cleaned_data['hours_needed']
            people_needed = form.cleaned_data['people_needed']
            Service.objects.create(name=name, description=description, hours_needed=hours_needed, people_needed=people_needed)
            return redirect('add_service')
        return render(request, 'form.html', {'form': form})


class ShowItem(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': Item.objects.all()})


class ShowService(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': Service.objects.all()})


class ShowSpot(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': Spot.objects.all()})


class ShowStatsView(View):

    def get(self, request):
        return render(request, 'stats.html')


class ShowScheduleView(View):

    def get(self, request):
        return render(request, 'schedule.html')


class ShowDetailSpot(View):        #dawny ShowDETAILBLOG

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


class ShowDetailItem(View):                         # dawny showdetailPOST
    def get(self, request, id):
        item = Item.objects.get(pk=id)
        return render(request, 'item_detail_view.html', {'item':item})


class ShowDetailService(View):                         # dawny showdetailPOST
    def get(self, request, id):
        service = Service.objects.get(pk=id)
        return render(request, 'service_detail_view.html', {'service':service})


class UpdateItemView(View):                           # dawny Update POST view

    def get(self, request, id):
        item = Item.objects.get(pk=id)
        form = AddItemModelForm(instance=item)
        return render(request, 'form.html', {'form':form})

    def post(self, request, id):
        item = Item.objects.get(pk=id)
        form = AddItemModelForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(reverse("update_item"), args=[id])
        return render(request, 'form.html', {'form': form})


class UpdateServiceView(View):                           # dawny Update POST view

    def get(self, request, id):
        service = Service.objects.get(pk=id)
        form = AddServiceModelForm(instance=service)
        return render(request, 'form.html', {'form':form})

    def post(self, request, id):
        service = Service.objects.get(pk=id)
        form = AddServiceModelForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect(reverse("update_service"), args=[id])
        return render(request, 'form.html', {'form': form})


class DeleteItemView(View):            # dawny delete POST

    def get(self, request, id):
        # item = Item.objects.get(pk=id)
        return render(request, 'form.html', {})

    def post(self, request, id):
        item = Item.objects.get(pk=id)
        item.delete()
        return redirect('show_item')


class DeleteServiceView(View):            # dawny delete POST

    def get(self, request, id):
        # service = Service.objects.get(pk=id)
        return render(request, 'form.html', {})

    def post(self, request, id):
        service = Service.objects.get(pk=id)
        service.delete()
        return redirect('show_service')


class ShowCollectionsView(View):

    def get(self, request):
        itemlist = ItemList.objects.all()
        servicelist = ServiceList.objects.all()
        return render(request, 'collectionsEXTEN.html', {'date':"DATE", "itemlist":itemlist, "servicelist":servicelist})


class ShowDetailItemList(View):

    def get(self, request):
        form = AddItemModelForm()
        itemlist = Item.objects.all()
        return render(request, 'item_list.html', {'itemlist': itemlist, 'form': form})

    def post(self, request):
        itemlist = Item.objects.all()
        form = AddItemModelForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.itemlist = itemlist
            item.save()
            return redirect(f"/collections/{itemlist}/")
        return render(request, 'form.html', {'form': form})
#
# class ShowDetailItemList(LoginRequiredMixin, ListView):
#     def get_queryset(self):
#         itemlist_id = ItemList.objects.get(id=self.request..id)
#         return Character.objects.filter(user=user_id)
#     template_name = 'metro_app/character_list.html'

class ShowDetailServiceList(View):

    def get(self, request):
        form = AddServiceModelForm()
        servicelist = Service.objects.all()
        return render(request, 'service_list.html', {'servicelist': servicelist, 'form': form})

    def post(self, request):
        servicelist = Service.objects.all()
        form = AddItemModelForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.servicelist = servicelist
            service.save()
            return redirect(f"/collections/{servicelist}/")
        return render(request, 'form.html', {'form': form})


class AddItemList(View):

    def get(self, request):
        form = AddItemList()
        return render(request, 'form2.html', {'form': form})

    def post(self, request):
        form = AddItemList(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            spot = form.cleaned_data['spot']
            items = form.cleaned_data['items']
            Service.objects.create(name=name, description=description, spot=spot, items=items)
            return redirect('add_item_list')
        return render(request, 'form2.html', {'form': form})


class AddServiceList(View):

    def get(self, request):
        form = AddServiceList()
        return render(request, 'form2.html', {'form': form})

    def post(self, request):
        form = AddServiceList(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            spot = form.cleaned_data['spot']
            services = form.cleaned_data['services']
            Service.objects.create(name=name, description=description, spot=spot, services=services)
            return redirect('add_service_list')
        return render(request, 'form2.html', {'form': form})


# class AddCommentView(View):
#
#     def get(self, request):
#         form = AddCommentModelForm()
#         return render(request, 'form.html', {'form':form})
#
#     def post(self, request):
#         form = AddCommentModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         return render(request, 'form.html', {'form': form})