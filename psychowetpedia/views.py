from django.shortcuts import render

from .models import Leczenie, Leki, Zaburzenia


def home(request):
    return render(request, 'psychowetpedia/home.html')


def dogs(request):
    disorders_dogs = Zaburzenia.objects.exclude(spec_gat='kot').order_by('nazwa')
    context = {'disorders_dogs': disorders_dogs}
    return render(request, 'psychowetpedia/dogs.html', context)


def cats(request):
    disorders_cats = Zaburzenia.objects.exclude(spec_gat='pies').order_by('nazwa')
    context = {'disorders_cats': disorders_cats}
    return render(request, 'psychowetpedia/cats.html', context)


def treatment_dogs(request, uuid):
    disorder_page = Zaburzenia.objects.get(uuid=uuid)
    treatments_dogs = Leczenie.objects.exclude(dawka_kot=None)
    context = {'disorder_page': disorder_page, 'treatments_dogs': treatments_dogs}

    return render(request, 'psychowetpedia/treatment_dogs.html', context)


def treatment_cats(request, uuid):
    disorder_page = Zaburzenia.objects.get(uuid=uuid)
    treatments_cats = Leczenie.objects.exclude(dawka_kot=None)
    context = {'disorder_page': disorder_page, 'treatments_cats': treatments_cats}

    return render(request, 'psychowetpedia/treatment_cats.html', context)


def drug_index(request):
    all_drugs = Leki.objects.all().order_by('nazwa')
    context = {'all_drugs': all_drugs}

    return render(request, 'psychowetpedia/drug_index.html', context)


def single_drug(request, uuid):
    drug_page = Leki.objects.get(uuid=uuid)
    all_drugs = Leki.objects.all().order_by('nazwa')
    context = {'all_drugs': all_drugs, 'drug_page': drug_page}

    return render(request, 'psychowetpedia/single_drug.html', context)



# Create your views here.
