from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('done/<int:id>/', views.done),
    path('undo/<int:id>/', views.undo),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
]