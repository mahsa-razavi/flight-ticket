from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', views.admin_view, name="admin"),
    path("login", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("flight", views.flight, name="flight"),
    path("review", views.review, name="review"),
    path("flight/ticket/book", views.book, name="book"),
    path('flight/bookings', views.bookings, name="bookings"),
    path('flight/ticket/api/<str:ref>', views.ticket_data, name="ticketdata"),
]