from django.core.management import BaseCommand
from catalog.models import Product, Category, Contacts
from skystore.settings import BASE_DIR
import json

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contacts.objects.all().delete()

        with open(BASE_DIR / 'catalog/fixtures/category.json', encoding='cp1251') as file:
            category_data = json.load(file)
            for item in category_data:
                Category.objects.create(
                    pk=item['pk'],
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                )

        with open(BASE_DIR / 'catalog/fixtures/contacts.json', encoding='cp1251') as file:
            contacts_data = json.load(file)
            for item in contacts_data:
                Contacts.objects.create(
                    pk=item['pk'],
                    country=item['fields']['country'],
                    inn=item['fields']['inn'],
                    address=item['fields']['address'],
                )

        with open(BASE_DIR / 'catalog/fixtures/product.json', encoding='cp1251') as file:
            product_data = json.load(file)
            for item in product_data:
                category_pk = item['fields']['category']
                category = Category.objects.get(pk=category_pk)
                Product.objects.create(
                    pk=item['pk'],
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                    image=item['fields']['image'],
                    category=category,
                    price=item['fields']['price'],
                    issued_date=item['fields']['issued_date'],
                    last_changed_date=item['fields']['last_changed_date'],
                )
