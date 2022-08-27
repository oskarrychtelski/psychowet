from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
# from .models import Profile


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
