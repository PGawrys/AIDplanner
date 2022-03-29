from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from AidplannerApp.forms import AddItemForm, AddItemModelForm, AddSpotForm, AddServiceForm, AddServiceModelForm
from AidplannerApp.models import Spot, Service, Item


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


class AddItemView(View):     #dawny addPOSTview

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


class ShowItem(View):         #dawny showPOST

    def get(self, request):
        return render(request, 'list.html', {'object_list': Item.objects.all()})


class ShowSpot(View):        #dawny ShowBLOG

    def get(self, request):
        return render(request, 'list.html', {'object_list': Spot.objects.all()})


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

class DeleteItemView(View):            # dawny delete POST

    def get(self, request, id):
        # post = Item.objects.get(pk=id)
        return render(request, 'form.html', {})

    def post(self, request, id):
        item = Item.objects.get(pk=id)
        item.delete()
        return redirect('show_item')


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