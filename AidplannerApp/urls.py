from django.contrib import admin
from django.urls import path

from AidplannerApp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('drugi/', views.IndexView2.as_view(), name='index2'),           # v
    path('add_spot/', views.AddSpot.as_view(), name='add_spot'),         # v
    path('collections/show_spot/', views.ShowSpot.as_view(), name='show_spot'),      # v
    path('add_item/', views.AddItemView.as_view(), name='add_item'),     # v
    path('collections/show_item/', views.ShowItem.as_view(), name='show_item'),      # v
    path('collections/show_service/', views.ShowService.as_view(), name='show_service'),  # v
    path('spot/<int:id>/', views.ShowDetailSpot.as_view(), name='show_detail_spot'),   # v
    path('item/<int:id>/', views.ShowDetailItem.as_view(), name='show_detail_item'),   # v
    path('update_item/<int:id>/', views.UpdateItemView.as_view(), name='update_item'),   # v
    path('delete_item/<int:id>/', views.DeleteItemView.as_view(), name='delete_item'),   # v
    path('service/<int:id>/', views.ShowDetailService.as_view(), name='show_detail_service'),  # v
    path('update_service/<int:id>/', views.UpdateServiceView.as_view(), name='update_service'),  # v
    path('delete_service/<int:id>/', views.DeleteServiceView.as_view(), name='delete_service'),  # v
    path('collections/', views.ShowCollectionsView.as_view(), name='collections'),
    path('collections/add_item_list/', views.AddItemList.as_view(), name='add_item_list'),
    path('collections/add_service_list/', views.AddServiceList.as_view(), name='add_service_list'),
    path('collections/itemlist/', views.ShowDetailItemList.as_view(), name='item_list'),
    path('collections/servicelist/', views.ShowDetailServiceList.as_view(), name='service_list'),
    path('stats/', views.ShowStatsView.as_view(), name='stats'),
    path('schedule/', views.ShowScheduleView.as_view(), name='schedule'),
    # path('create_post_generic_view/', generic_views.CreatePostView.as_view(), name='gen_post_create_view'),
    # path('dpv_gen/<int:pk>/', generic_views.DetailPostVIew.as_view(), name='det_post_view_gen')
]