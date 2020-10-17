from django import forms
from django.core import validators
from .models import Protokoll, ProtokollFach


#Klassen die benötigt werden um etwas in Models abzuspeichern hier für Model Protokoll
class Protokollspeichern(forms.ModelForm):
    class Meta:
        model = Protokoll
        fields = ['Thema', 'Experimente', 'Theorie',]
#Klassen die benötigt werden um etwas in Models abzuspeichern hier für Model ProtokollFach
class ProtokollFachspeichern(forms.ModelForm):
    class Meta:
        model = ProtokollFach
        fields = ['Fachbereich']
