from django.contrib import admin
from django.urls import path

from AidplannerApp import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('drugi/', views.IndexView2.as_view(), name='index2'),           # v
    path('add_spot/', views.AddSpot.as_view(), name='add_spot'),         # v
    path('show_spot/', views.ShowSpot.as_view(), name='show_spot'),      # v
    path('add_item/', views.AddItemView.as_view(), name='add_item'),     # v
    path('show_item/', views.ShowItem.as_view(), name='show_item'),      # v
    path('spot/<int:id>/', views.ShowDetailSpot.as_view(), name='show_detail_spot'),   # v
    path('item/<int:id>/', views.ShowDetailItem.as_view(), name='show_detail_item'),   # v
    # path('add_comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('update_item/<int:id>/', views.UpdateItemView.as_view(), name='update_item'),   # v
    path('delete_item/<int:id>/', views.DeleteItemView.as_view(), name='delete_item'),   # v
    # path('create_post_generic_view/', generic_views.CreatePostView.as_view(), name='gen_post_create_view'),
    # path('dpv_gen/<int:pk>/', generic_views.DetailPostVIew.as_view(), name='det_post_view_gen')
]