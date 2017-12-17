from django import forms

class UploadDataForm(forms.Form):
    File = forms.FileField()
    CHOICES=[('Models','Models'),
             ('Variants','Variants'),
             ('Listings','Listings')
             ]
    Option = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
