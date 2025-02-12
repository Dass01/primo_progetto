from django.shortcuts import render

eventi = [
    {"titolo": "Giornata dello Sport", "data": "2025-03-01", "descrizione": "Una giornata dedicata alle attività sportive per tutte le classi.", "partecipanti": 120},
    {"titolo": "Conferenza sulla Tecnologia", "data": "2025-04-15", "descrizione": "Un incontro con esperti di tecnologia per discutere le ultime innovazioni.", "partecipanti": 80},
    {"titolo": "Festa di Fine Anno", "data": "2025-06-20", "descrizione": "Un evento per celebrare la fine dell'anno scolastico.", "partecipanti": 200},
    {"titolo": "Settimana della Scienza", "data": "2025-05-10", "descrizione": "Esperimenti e laboratori per tutte le classi.", "partecipanti": 150},
    {"titolo": "Giornata della Lettura", "data": "2025-02-21", "descrizione": "Attività e letture condivise in biblioteca.", "partecipanti": 50},
]



def view_a(request):


    context={"eventi":eventi}
    return render(request, "elencoTitoliEventi.html",context)

