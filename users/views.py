from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Notatki
from .forms import NotesForm


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Podany użytkownik nie istnieje.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            print('Nazwa użytkownika lub/i hasło są niepoprawne.')
    return render(request, 'users/register_login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def notes(request):
    if Notatki.objects.filter(autor=request.user).exists():
        author_notes = Notatki.objects.filter(autor=request.user)
    else:
        author_notes = None

    context = {'author_notes': author_notes}
    return render(request, 'users/read_notes.html', context)


@login_required(login_url='login')
def createNotes(request):
    form = NotesForm()

    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')

    context = {'form': form}
    return render(request, 'users/note_form.html', context)


@login_required(login_url='login')
def updateNotes(request, uuid):
    note = Notatki.objects.get(id=uuid)
    form = NotesForm(instance=note)

    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')

    context = {'form': form}
    return render(request, 'users/note_form.html', context)