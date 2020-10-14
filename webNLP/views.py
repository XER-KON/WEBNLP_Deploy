from django.shortcuts import render
from .import forms
from .models import Protokoll, ProtokollFach
from .forms import Protokollspeichern, ProtokollFachspeichern

# Funktion die dafür zuständig ist, dass die Nutzereingaben unter Model ProtokollFach gespeichert werden
# und und die Infos aus POST von home.html abspeichert.
def home(request):
    Fachspeichern = forms.ProtokollFachspeichern()
    if request.method == 'POST':
        Fachspeichern = forms.ProtokollFachspeichern(request.POST)
        if Fachspeichern.is_valid():
            Fachspeichern.save()

    return render(request,"home.html",{'Fachspeichern':Fachspeichern})

# Funktion die dafür zuständig ist, dass die Nutzereingaben unter Model Protokoll gespeichert werden
# und und die Infos aus POST von form_page.html abspeichert.
def form_Thema1_view(request):
    formspeichern = forms.Protokollspeichern()

    if request.method == 'POST':
        formspeichern = forms.Protokollspeichern(request.POST)
        if formspeichern.is_valid():
            formspeichern.save()


    return render(request,"form_page.html",{'formspeichern':formspeichern})

#Wenn du eingegeben Informationen aus Datenbank abrufen willst, einfach
#+form.cleaned_data[Name der Unterklasse]. Einfach ignorieren das ist für mich


#Diese Funktion ignorieren die ist von der alten website und gehör zu regex.html.
# Das ist aber ein gutes Beispiel, wie man die eingegeben Info überprüfen kann und
#auf diese reagiert. Zunächst wird Telefonnummer definiert.
def regex(request):
    import re
    if request.method=="POST":
        Telefonnummer=r'\d{4}-\d{7}'
        regex_area=request.POST['regexform']
        #Eingaben in Textfeld werden als eine Variable definiert
        regex_phone=re.findall(Telefonnummer,regex_area)
        #Eingaben werden nach Telefonnummer abgesucht
        return render(request, 'regex.html',{'rphone':regex_phone})
        #weiterleiten an die regex.html Seite
    else:
        return render(request, "home.html",{})
