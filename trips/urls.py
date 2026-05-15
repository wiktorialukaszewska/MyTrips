from django.urls import path
from .views import place_detail, trip_map, add_place

urlpatterns = [
    path("place/<int:pk>/", place_detail, name="place-detail"),
    path("trip/<int:trip_pk>/map/", trip_map, name="trip-map"),
    path("trip/<int:trip_pk>/add-place/", add_place, name="add-place"),
]