from django.urls import path
from .views import (ItemDetailView, HomeView,add_to_cart,
    remove_from_cart,CheckoutView,
    remove_single_item_from_cart,OrderSummaryView,search
)
app_name = 'core'
urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('product/<slug>/', ItemDetailView.as_view(), name='product'),
  path('check/', CheckoutView.as_view(), name='checkout'),
  path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
  path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
  path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,name='remove-single-item-from-cart'),
  path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
  path('search/',search),      
    ]
