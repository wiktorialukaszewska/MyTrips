from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Place, Trip
from .forms import PlaceForm
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
            place.latitude = request.POST.get('latitude')
            place.longitude = request.POST.get('longitude')
            place.save()
            return redirect('trip-map', trip_pk=trip_pk)
    else:
        form = PlaceForm(initial={'trip': trip})
    return render(request, 'trips/add_place.html', {
        'form': form,
        'trip': trip,
        'google_api_key': settings.GOOGLE_MAPS_API_KEY,
    })