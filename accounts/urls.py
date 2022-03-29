from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('userlist/', views.UserListView.as_view(), name='userlist'),
    path('user_perm/<int:id>/', views.UserPermSettings.as_view(), name='user_perm'),
]