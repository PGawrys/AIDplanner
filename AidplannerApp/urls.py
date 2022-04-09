from django.contrib import admin
from django.urls import path

from AidplannerApp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),   # 1 test
    path('collections/add_spot/', views.AddSpot.as_view(), name='add_spot'),         # 2 testy
    path('collections/show_spot/', views.ShowSpot.as_view(), name='show_spot'),      # 1 test
    path('show_spot/<int:id>/', views.ShowDetailSpot.as_view(), name='show_detail_spot'),   # 2 testy
    path('update_item/<int:id>/', views.UpdateItemView.as_view(), name='update_item'),   #
    path('delete_item/<int:id>/', views.DeleteItemView.as_view(), name='delete_item'),   #
    path('collections/update_spot/<int:id>/', views.UpdateSpotView.as_view(), name='update_spot'),   #
    path('collections/delete_spot/<int:id>/', views.DeleteSpotView.as_view(), name='delete_spot'),
    path('update_service/<int:id>/', views.UpdateServiceView.as_view(), name='update_service'),  #
    path('delete_service/<int:id>/', views.DeleteServiceView.as_view(), name='delete_service'),  #
    path('collections/', views.ShowCollectionsView.as_view(), name='collections'),
    path('collections/add_collection_item/', views.AddCollectionItem.as_view(), name='add_collection_item'),
    path('collections/add_collection_service/', views.AddCollectionService.as_view(), name='add_collection_service'),
    path('collections/itemlist/', views.ShowDetailItemList.as_view(), name='item_list'),
    path('collections/servicelist/', views.ShowDetailServiceList.as_view(), name='service_list'),
    path('stats/', views.ShowStatsView.as_view(), name='stats'),
    path('schedule/', views.ShowScheduleView.as_view(), name='schedule'),
    path('collections/update_item_collection/<int:id>/', views.UpdateItemCollectionView.as_view(), name='update_item_collection'),
    path('collections/update_service_collection/<int:id>/', views.UpdateServiceCollectionView.as_view(), name='update_service_collection'),
    path('collections/delete_item_collection/<int:id>/', views.DeleteItemCollectionView.as_view(), name='delete_item_collection'),
    path('collections/delete_service_collection/<int:id>/', views.DeleteServiceCollectionView.as_view(), name='delete_service_collection'),
    ]
