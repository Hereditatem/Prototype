
from django import forms 

class FragmentForm(forms.Form):
    backscan = forms.ImageField()
    frontscan = forms.ImageField()
    width = forms.DecimalField()
    height = forms.DecimalField()
    thickness = forms.DecimalField()