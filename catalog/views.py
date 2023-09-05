from django.shortcuts import render
from catalog.models import Product, Contacts


def homepage(request):
    context = {
        'title': 'skystore',
        'products': Product.objects.all()[:5]

    }
    return render(request, "catalog/homepage.html", context=context)

def contacts(request):
    data = {}
    if request.method == "POST":
        data['name'] = request.POST.get('name')
        data['phone'] = request.POST.get('phone')
        data['message'] = request.POST.get('message')
        print(data)
    context = {
        'title': 'contacts',
        'contacts': Contacts.objects.first()
    }
    return render(request, "catalog/contacts.html", context=context)