from django.urls import path
from catalog.views import ProductListView, ContactsListView, ProductDetailView


name_app = "catalog"

urlpatterns = [
    path('', ProductListView.as_view(), name="homepage"),
    path('contacts/', ContactsListView.as_view(), name="contacts"),
    path('product/<pk>', ProductDetailView.as_view(), name="product"),
]
