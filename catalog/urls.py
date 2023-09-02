from django.urls import path
from catalog.views import homepage, contacts

name_app = "catalog"

urlpatterns = [
    path('', homepage, name="homepage"),
    path('contacts/', contacts, name="contacts"),

]
