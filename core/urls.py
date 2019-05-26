from django.urls import path
from . import views


urlpatterns =[
   
    path('home/', views.HomeView.as_view(), name='home'),
    path('members/', views.MembersView.as_view(), name='members'),
    path('base/', views.base_view.as_view(), name='base'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),


]

