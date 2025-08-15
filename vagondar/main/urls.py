from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainViews.as_view(), name="main"),
    path('delete_wagon/<int:pk>/', views.DeleteWagonView.as_view(), name='delete_wagon'),
    path('delete_event/<int:pk>/', views.DeleteEventView.as_view(), name="delete_event"),
    path('tariff_history/', views.TariffHistoryViews.as_view(), name="tariff_history"),
    path("add_event/", views.AddEventView.as_view(), name="add_event")
]
