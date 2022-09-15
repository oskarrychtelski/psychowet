from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Notatki
from .forms import NotesForm, ContactForm


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Podany użytkownik nie istnieje.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nazwa użytkownika lub/i hasło są niepoprawne.')

    context = {'page': page}
    return render(request, 'users/register_login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Konto zostało stworzone!')

            login(request, user)
            return redirect('index')

        else:
            messages.success(request, 'Nastąpił błąd podczas rejestracji!')

    context = {'page': page, 'form': form}
    return render(request, 'users/register_login.html', context)


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
            instance = form.save(commit=False)
            instance.autor = request.user
            instance.save()
            return redirect('notes')

    context = {'form': form}
    return render(request, 'users/note_form.html', context)


@login_required(login_url='login')
def updateNotes(request, uuid):
    note = Notatki.objects.get(uuid=uuid)
    form = NotesForm(instance=note)

    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')

    context = {'form': form}
    return render(request, 'users/note_form.html', context)


def deleteNotes(request, uuid):
    note = Notatki.objects.get(uuid=uuid)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    context = {'object': note}
    return render(request, 'users/delete_template.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            messages.success(request, 'Mail został wysłany!')

            html = render_to_string('users/contact_form.html', {
                                    'name': name,
                                    'email': email,
                                    'content': content
            })

            send_mail('Topic', 'Message', 'noreply@psychowet.com', ['oskar.rychtelski@gmail.com'], html_message=html)
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'users/contact.html', context)