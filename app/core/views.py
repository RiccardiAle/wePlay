from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, ReservationForm


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Creazione dell'utente
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            user.save()

            # Autenticazione dell'utente e login automatico
            user = authenticate(username=username, password=password)
            login(request, user)

            # Reindirizza l'utente alla pagina di conferma della registrazione o altrove
            return redirect('')  # Aggiungi l'URL desiderato

    else:
        form = RegistrationForm()  # Mostra il modulo di registrazione vuoto

    return render(request, 'registration/register.html', {'form': form})

@login_required
@csrf_protect
def book_field(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Elabora la prenotazione e invia una notifica al proprietario
            reservation = form.save(commit=False)
            reservation.user = request.user  # Collega la prenotazione all'utente attuale
            reservation.save()
            return redirect('booking_success')  # Aggiungi l'URL desiderato

    else:
        form = ReservationForm()  # Mostra il modulo di prenotazione vuoto

    return render(request, 'booking/book.html', {'form': form})