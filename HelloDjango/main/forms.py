from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': 'Введите имя'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", 'placeholder': '8(___)___-__-__'}))
