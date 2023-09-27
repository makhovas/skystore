from django import forms
from catalog.models import Product, Version
from skystore.settings import FORBIDDEN_WORDS


class ProductForm(forms.ModelForm):
    version = forms.ModelChoiceField(queryset=Version.objects.all(), required=False, empty_label="Выберите версию")
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category', 'version',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        if cleaned_data in FORBIDDEN_WORDS:
            raise forms.ValidationError('Hельзя загружать запрещенные продукты на платформу')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']

        if cleaned_data in FORBIDDEN_WORDS:
            raise forms.ValidationError('Hельзя загружать запрещенные продукты на платформу')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
