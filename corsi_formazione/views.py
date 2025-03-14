from django.shortcuts import render, get_object_or_404
from .models import Corso
import datetime

#index contenente tutti i link delle pagine di quest'app
def index_corsi(request):
    return render(request,"index_corsi.html")

#Elenco dei corsi ordinati per data di inizio
def view_a(request):

    corsi_ordinati_inizio = Corso.objects.order_by('-data_inizio')
    
    context={"corsi_ordinati_inizio":corsi_ordinati_inizio,}
    return render(request, "view_a.html",context)

#Dettagli di un corso cliccato sulla view a.
def view_b(request, pk):
    corso=get_object_or_404(Corso, pk=pk)
    context={"corso":corso}
    return render(request, "view_b.html",context)

#Elenco dei corsi che iniziano dopo il 01/05/2025.
def view_c(request):
    corsi_dopo_data = Corso.objects.filter(data_inizio__gt=datetime.date(2025, 5, 1))
    context={"corsi_dopo_data":corsi_dopo_data,}
    return render(request, "view_c.html",context)

#Elenco dei corsi con meno di 20 posti disponibili.
def view_d(request):
    corsi_meno20 = Corso.objects.filter(posti_disponibili__lte=20)
    context={"corsi_meno20":corsi_meno20,}
    return render(request, "view_d.html",context)

#Elenco dei corsi che terminano entro il 30/04/2025.
def view_e(request):
    corsi_terminati_entro = Corso.objects.filter(data_fine__lt=datetime.date(2025, 4, 30))
    context={"corsi_terminati_entro":corsi_terminati_entro,}
    return render(request, "view_e.html",context)

#Visualizzare il corso con più posti disponibili, quello con meno posti e il totale dei posti disponibili:
def view_f(request):
    corso_piu_posti = Corso.objects.order_by('-posti_disponibili').first()
    corso_meno_posti = Corso.objects.order_by('posti_disponibili').first()

    elencoCorsi=Corso.objects.all()
    nTot=0
    for corso in elencoCorsi:
        nTot+=corso.posti_disponibili

    context={"corso_piu_posti":corso_piu_posti,"corso_meno_posti":corso_meno_posti,"nTot":nTot}
    return render(request, "view_f.html",context)








    
