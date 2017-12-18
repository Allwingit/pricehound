from django import forms
from .models import Brand,Category
BRAND_CHOICES=(tuple([brand,brand]) for brand in Brand.objects.all())
CATEGORY_CHOICES=(tuple([category,category]) for category in Category.objects.all())
CHOICES=[('Models','Models'),
         ('Variants','Variants'),
         ('Listings','Listings')
         ]

class UploadDataForm(forms.Form):
    Brand_Name =forms.CharField(label="Select Brand :",widget=forms.Select(choices=BRAND_CHOICES))
    Category_Name =forms.CharField(label="Select Category:",widget=forms.Select(choices=CATEGORY_CHOICES))
    File = forms.FileField()
    Option = forms.ChoiceField(label="Select Option",choices=CHOICES, widget=forms.RadioSelect())
