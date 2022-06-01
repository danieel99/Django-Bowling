from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from .models import Zawodnik, Klub, Rezerwacja
from .forms import ZawodnikForm , RezerwacjaForm, KlubForm
from django.db.models import DateTimeField
from django.db.models.functions import Trunc
import datetime 
import os
import csv
from django.core.paginator import Paginator

now = datetime.datetime.now()


def home(request):
    return render(request, 'home.html')

def kluby(request):
    return render(request, 'kluby.html')

def cennik(request):
    return render(request, 'cennik.html')

def potwierdzenie(request):
    return render(request, 'potwierdzenie.html')

def zajete(request):
    return render(request, 'zajete.html')

def zapisy(request, pk_klubu):
    klub = Klub.objects.get(pk=pk_klubu)
    if request.method == "POST":
        form = ZawodnikForm(request.POST)
        if form.is_valid():
            obj = form.instance
            obj.save()
            klub.czlonkowie.add(obj)
            klub.save()
            return HttpResponseRedirect('/potwierdzenie')
    else:
        form = ZawodnikForm
    return render(request, 'zapisy.html', {
        'form': form, 
        })

def rezerwacja(request):
    dzien = request.POST.get('dzien')
    godzina = request.POST.get('godziny')
    tor = request.POST.get('tor')

    terminy = Rezerwacja.objects.filter(dzien=dzien).filter(godziny=godzina).filter(tor=tor)
    if request.method == "POST":
        form = RezerwacjaForm(request.POST)
        if form.is_valid() and len(terminy)==0:
            form.save()
            return HttpResponseRedirect('/potwierdzenie')
        else:
            return HttpResponseRedirect('/zajete')
    else:
        form = RezerwacjaForm

    return render(request, 'rezerwacja.html', {
        'form': form, 
        })

def zawodnicy(request):
    zawodnicy = Zawodnik.objects.all()
    p = Paginator(Zawodnik.objects.all(), 2)
    page = request.GET.get('page')
    zawodnicy_p = p.get_page(page)
    nums = "a" * zawodnicy_p.paginator.num_pages
    return render(request, 'zawodnicy.html',{
        'zawodnicy': zawodnicy,
        'zawodnicy_p': zawodnicy_p,
        'nums': nums
    })

def klubowi_gracze(request, klub_id):
    klub  = Klub.objects.get(pk=klub_id)
    zawodnicy = klub.czlonkowie.all()
    return render(request, 'klubowi_gracze.html',{
         'zawodnicy': zawodnicy
         })

def rezerwacje(request):
    rezerwacje = Rezerwacja.objects.order_by('dzien','godziny')
    return render(request, 'rezerwacje.html',{
        'rezerwacje': rezerwacje
    })

def pobierz(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['Imię', 'Nazwisko', 'Płeć', 'Pseudonim'])

    for zawodnik in Zawodnik.objects.all().values_list('imie', 'nazwisko', 'plec', 'pseudonim'):
        writer.writerow(zawodnik)
    
    response['Content-Disposition'] = 'attachment; filename="Django_lista_czlonkow.csv"'
    return response

def wykres(request):
    return render(request, 'wykres.html')

def api_wykres(request):
    kregle_gracze = Klub.objects.get(pk=3)
    kregle_gracze = kregle_gracze.czlonkowie.all().count()
    kregle_gracze = int(kregle_gracze)

    bilard_gracze = Klub.objects.get(pk=4)
    bilard_gracze = bilard_gracze.czlonkowie.all().count()
    bilard_gracze = int(bilard_gracze)

    lotki_gracze = Klub.objects.get(pk=5)
    lotki_gracze = lotki_gracze.czlonkowie.all().count()
    lotki_gracze = int(lotki_gracze)

    labels = ['Kregle Club', 'Bilard Club', 'Dart Club']
    counts = [kregle_gracze, bilard_gracze, lotki_gracze]

    data = {'labels': labels, 'counts': counts}
    return JsonResponse(data)