from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Place, Trip, Expense
from .forms import PlaceForm, TripForm, ExpenseForm
import json

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, "trips/place_detail.html", {
        "place": place,
        "google_api_key": settings.GOOGLE_MAPS_API_KEY
    })

def trip_map(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    places = Place.objects.filter(trip=trip)
    places_data = [
        {
            "name": p.name,
            "lat": p.latitude,
            "lng": p.longitude,
            "notes": p.notes,
        }
        for p in places
        if p.latitude and p.longitude
    ]
    return render(request, "trips/trip_map.html", {
        "trip": trip,
        "places_json": json.dumps(places_data),
        "google_api_key": settings.GOOGLE_MAPS_API_KEY,
    })

def add_place(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.trip = trip
            place.latitude = request.POST.get('latitude')
            place.longitude = request.POST.get('longitude')
            place.save()
            return redirect('place-list', trip_pk=trip_pk)
    else:
        form = PlaceForm()
    return render(request, 'trips/add_place.html', {
        'form': form,
        'trip': trip,
        'google_api_key': settings.GOOGLE_MAPS_API_KEY,
    })

def trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trips/trip_list.html', {
        'trips': trips,
    })

def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trip-list')
    else:
        form = TripForm()
    return render(request, 'trips/add_trip.html', {
        'form': form,
    })

def place_list(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    places = Place.objects.filter(trip=trip)
    return render(request, 'trips/place_list.html', {
        'trip': trip,
        'places': places,
    })

def edit_trip(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trip-list')
    else:
        form = TripForm(instance=trip)
    return render(request, 'trips/edit_trip.html', {
        'form': form,
        'trip': trip,
    })

def delete_trip(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('trip-list')
    return render(request, 'trips/delete_trip.html', {
        'trip': trip,
    })

def delete_place(request, trip_pk, place_pk):
    place = get_object_or_404(Place, pk=place_pk)
    if request.method == 'POST':
        place.delete()
        return redirect('place-list', trip_pk=trip_pk)
    return render(request, 'trips/delete_place.html', {
        'place': place,
        'trip_pk': trip_pk,
    })

def expense_list(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    expenses = Expense.objects.filter(trip=trip)
    total = sum(e.amount for e in expenses)
    return render(request, 'trips/expense_list.html', {
        'trip': trip,
        'expenses': expenses,
        'total': total,
    })

def add_expense(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.trip = trip
            expense.save()
            return redirect('expense-list', trip_pk=trip_pk)
    else:
        form = ExpenseForm()
    return render(request, 'trips/add_expense.html', {
        'form': form,
        'trip': trip,
    })

def delete_expense(request, trip_pk, expense_pk):
    expense = get_object_or_404(Expense, pk=expense_pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense-list', trip_pk=trip_pk)
    return render(request, 'trips/delete_expense.html', {
        'expense': expense,
        'trip_pk': trip_pk,
    })