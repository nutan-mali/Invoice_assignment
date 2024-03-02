from django.urls import path

from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("invoice/", views.invoice, name="invoice"),
    path("invoice/<int:invoice_id>/", views.invoice_detail, name="invoice_detail"),
]