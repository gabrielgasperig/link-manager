from django.urls import path
from . import views

urlpatterns = [
    path('', views.link_list, name='link_list'),
    path('add/', views.add_link, name='add_link'),
    path('edit/<int:pk>/', views.edit_link, name='edit_link'),
    path('delete/<int:pk>/', views.delete_link, name='delete_link'),
    path('share/<int:pk>/', views.share_link, name='share_link'),
]
