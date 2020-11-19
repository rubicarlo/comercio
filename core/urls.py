from django.urls import path
from .views import (
    checkout,
    HomeView,
    ItemDetailView,
    anadir_al_carro,
)

app_name = 'core'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('checkout/',checkout, name='checkout'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('carrito/<slug>/', anadir_al_carro, name='carrito')
]
