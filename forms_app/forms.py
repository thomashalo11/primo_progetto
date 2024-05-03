from django import forms
from .models import Contatto
class FormContatto(forms.ModelForm):
    nome = forms.CharField()
    cognome = forms.CharField()
    email = forms.EmailField()
    contenuto = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Area testuale, scrivi pure :)"}))
    class Meta:
        model = Contatto
        fields = "__all__"