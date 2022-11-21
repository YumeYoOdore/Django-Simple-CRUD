from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('remove/<int:element_id>/', views.remove, name="remove"),
    path('edit/<int:element_id>/', views.edit, name="edit"),
]
