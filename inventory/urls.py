from django.urls import path 
from . import views 

urlpatterns = [
    path('add-item/', views.add_item, name='add-item'), 
    path('update-item/<int:pk>/', views.update_item, name='update-item'), 
    path('delete-item/<int:pk>/', views.delete_item, name='delete-item'), 
    path('item-details/<int:pk>/', views.item_details, name='item-details'), 
    path('all-items/', views.all_items, name='all-items'), 
    path('give-item/<int:pk>/', views.give_item, name='give-item'), 
    path('receive-item/<int:pk>/', views.receive_item, name='receive-item'), 
    path('search-item/', views.search_item, name='search-item')
]