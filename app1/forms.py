from django import forms

class Salman(forms.Form):
    name=forms.CharField(max_length=70,label_suffix=':')
    email=forms.EmailField(max_length=70,label_suffix=':')
    password=forms.CharField(max_length=70,label_suffix=':')
    id=forms.IntegerField(max_value=70,label_suffix=':')
    dob=forms.DateField()