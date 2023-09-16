from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product, Contacts, Category


# def homepage(request):
#     context = {
#         'title': 'skystore',
#         'products': Product.objects.all()[:5]
#
#     }
#     return render(request, "catalog/homepage.html", context=context)

# def contacts(request):
#     data = {}
#     if request.method == "POST":
#         data['name'] = request.POST.get('name')
#         data['phone'] = request.POST.get('phone')
#         data['message'] = request.POST.get('message')
#         print(data)
#     context = {
#         'title': 'contacts',
#         'contacts': Contacts.objects.first()
#     }
#     return render(request, "catalog/contacts.html", context=context)

class ContactsListView(ListView):
    model = Contacts
    template_name = 'catalog/contacts.html'
    context_object_name = 'contacts'
    queryset = Contacts.objects.first()


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/homepage.html'
    queryset = Product.objects.all()[:5]
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    # template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {
#         'title': product.name,
#         'product': product,
#     }
#     return render(request, "catalog/product_detail.html", context=context)
