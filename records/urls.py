from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_records, name='list'),
    path('add/', views.add_record, name='add'),
    path('edit/<int:pk>/', views.edit_record, name='edit'),
    path('delete/<int:pk>/', views.delete_record, name='delete'),
]