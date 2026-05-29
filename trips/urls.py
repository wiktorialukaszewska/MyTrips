from django.urls import path
from .views import place_detail, trip_map, add_place, trip_list, add_trip, place_list, edit_trip, delete_trip, delete_place, expense_list, add_expense, delete_expense

urlpatterns = [
    path("", trip_list, name="trip-list"),
    path("place/<int:pk>/", place_detail, name="place-detail"),
    path("trip/<int:trip_pk>/map/", trip_map, name="trip-map"),
    path("trip/<int:trip_pk>/add-place/", add_place, name="add-place"),
    path("trip/<int:trip_pk>/places/", place_list, name="place-list"),
    path("trip/add/", add_trip, name="add-trip"),
    path("trip/<int:trip_pk>/edit/", edit_trip, name="edit-trip"),
    path("trip/<int:trip_pk>/delete/", delete_trip, name="delete-trip"),
    path("trip/<int:trip_pk>/place/<int:place_pk>/delete/", delete_place, name="delete-place"),
    path("trip/<int:trip_pk>/expenses/", expense_list, name="expense-list"),
    path("trip/<int:trip_pk>/add-expense/", add_expense, name="add-expense"),
    path("trip/<int:trip_pk>/expense/<int:expense_pk>/delete/", delete_expense, name="delete-expense"),
]