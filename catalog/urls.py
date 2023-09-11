from django.urls import path
from catalog.views import homepage, contacts, product_detail
from django.conf.urls.static import static
from django.conf import settings

name_app = "catalog"

urlpatterns = [
    path('', homepage, name="homepage"),
    path('contacts/', contacts, name="contacts"),
    path('product/<pk>', product_detail, name="product"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
