from django.urls import path
from catalog.views import ProductListView, ContactsListView, ProductDetailView, ProductCreateView

app_name = "catalog"

urlpatterns = [
    path('', ProductListView.as_view(), name="homepage"),
    path('create/', ProductCreateView.as_view(), name="create_product"),
    path('contacts/', ContactsListView.as_view(), name="contacts"),
    path('product/<pk>', ProductDetailView.as_view(), name="product"),
]
