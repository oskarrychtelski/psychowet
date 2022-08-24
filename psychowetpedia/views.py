from django.shortcuts import render

from .models import Leczenie, Leki, Zaburzenia


def home(request):
    return render(request, 'psychowetpedia/home.html')


def psy(request):
    zaburzenia_psy = Zaburzenia.objects.exclude(spec_gat='kot').order_by('nazwa')
    context = {'zaburzenia_psy': zaburzenia_psy}
    return render(request, 'psychowetpedia/psy.html', context)


def koty(request):
    zaburzenia_koty = Zaburzenia.objects.exclude(spec_gat='pies').order_by('nazwa')
    context = {'zaburzenia_koty': zaburzenia_koty}
    return render(request, 'psychowetpedia/koty.html', context)


def leczenie_zaburzen_psy(request, uuid):
    zaburzenie_strona = Zaburzenia.objects.get(uuid=uuid)
    leczenie_psy = Leczenie.objects.exclude(dawka_kot=None)
    context = {'zaburzenie_strona': zaburzenie_strona, 'leczenie_psy': leczenie_psy}

    return render(request, 'psychowetpedia/leczenie_zaburzen_psy.html', context)


def leczenie_zaburzen_koty(request, uuid):
    zaburzenie_strona = Zaburzenia.objects.get(uuid=uuid)
    leczenie_koty = Leczenie.objects.exclude(dawka_kot=None)
    context = {'zaburzenie_strona': zaburzenie_strona, 'leczenie_koty': leczenie_koty}

    return render(request, 'psychowetpedia/leczenie_zaburzen_koty.html', context)


def leki(request):
    leki_wszystkie = Leki.objects.all().order_by('nazwa')
    context = {'leki_wszystkie': leki_wszystkie}

    return render(request, 'psychowetpedia/leki.html', context)


def lek(request, uuid):
    lek_strona = Leki.objects.get(uuid=uuid)
    leki_wszystkie = Leki.objects.all().order_by('nazwa')
    context = {'leki_wszystkie': leki_wszystkie, 'lek_strona': lek_strona}

    return render(request, 'psychowetpedia/lek.html', context)



# Create your views here.
