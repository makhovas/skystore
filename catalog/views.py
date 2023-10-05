from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.forms import formset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contacts, Category, Version


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
    #queryset = Contacts.objects.first()


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/homepage.html'
    #queryset = Product.objects.all()[:5]
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()[:6]
        for product in products:
            product.active_version = product.version.filter(is_active=True).first()
        context['products'] = products
        return context

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    # template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        if settings.CACHE_ENABLED:
            key = 'category_list'
            category_list = cache.get(key)
            if category_list is None:
                category_list = Category.objects.all()
                cache.set(key, category_list)
        else:
            category_list = Category.objects.all()

        context_data['category'] = category_list
        return context_data

# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {
#         'title': product.name,
#         'product': product,
#     }
#     return render(request, "catalog/product_detail.html", context=context)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:homepage')
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        VersionFormset = formset_factory(VersionForm, extra=1)
        context['version_formset'] = VersionFormset()
        return context

    def form_valid(self, form):
        new_product = form.save()
        new_product.owner = self.request.user
        new_product.save()
        if form.cleaned_data['version']:
            selected_version = form.cleaned_data['version']
            selected_version.product.add(new_product)
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:homepage')
    form_class = ProductForm
