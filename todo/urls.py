from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('done/<int:id>/', views.done),
    path('undo/<int:id>/', views.undo),
    path('delete/<int:id>/', views.delete),
]