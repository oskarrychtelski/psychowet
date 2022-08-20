from django.shortcuts import render

from .models import Leczenie, Leki

def psycholator(request):
    return render(request, 'psycholator/psycholator.html')

def psy(request):
    zaburzenia_psy = Leczenie.objects.values_list('zaburzenie', flat=True).exclude(dawka_pies=None).distinct().order_by('zaburzenie')
    leczenie_psy = Leczenie.objects.exclude(dawka_pies=None)
    results = zip(zaburzenia_psy, leczenie_psy)
    context = {'results': results}
    return render(request, 'psycholator/psy.html', context)

def koty(request):
    zaburzenia_koty = Leczenie.objects.values_list('zaburzenie', flat=True).exclude(dawka_kot=None).distinct().order_by('zaburzenie')
    leczenie_koty = Leczenie.objects.exclude(dawka_kot=None)
    results = zip(zaburzenia_koty, leczenie_koty)
    context = {'results': results}
    return render(request, 'psycholator/koty.html', context)

def leczenie_zaburzen_psy(request, pk):
    leczenie_strona = Leczenie.objects.get(id=pk)
    return render(request, 'psycholator/leczenie_zaburzen.html', {'leczenie_strona': leczenie_strona})

def leczenie_zaburzen_koty(request, pk):
    leczenie_strona = Leczenie.objects.get(id=pk)
    return render(request, 'psycholator/leczenie_zaburzen.html', {'leczenie_strona': leczenie_strona})

# Create your views here.
