from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Invoice, InvoiceDetails
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.

def index(request):
    return HttpResponse("Hello! This is my Invoice and Invoice Details Assignment. You can test POST, GET, PUT, and DELETE requests here.")

@csrf_exempt
def invoice(request):
    if request.method == "POST":
        # Parse the JSON data from the request body
        context = json.loads(request.body)
        print("Received Data is ",context) 
        # Create a new Invoice object
        invoices = Invoice.objects.create(
            date=context['date'],
            cust_name=context['cust_name']
        )
        return JsonResponse({'message': 'Invoice created successfully'})

    elif request.method == "GET":
        # Retrieve all existing Invoice objects from the database
        invoices = Invoice.objects.all().values('id', 'date', 'cust_name')
        data = list(invoices)
        return JsonResponse(data, safe=False)

@csrf_exempt
def invoice_detail(request, invoice_id):
    try:
        # Retrieve the Invoice object based on the provided ID
        invoice = Invoice.objects.get(id=invoice_id)
    except Invoice.DoesNotExist:
        return JsonResponse({'error': 'Invoice not found'}, status=404)

    if request.method == 'GET':
        # Retrieve details associated with the invoice
        details = InvoiceDetails.objects.filter(invoice=invoice)
        # Construct the response data
        data = {
            'id': invoice.id,
            'date': invoice.date,
            'cust_name': invoice.cust_name,
            'details': [{'description': detail.description, 'quantity': detail.quantity, 
                         'unit_price': detail.unit_price, 'price': detail.price} for detail in details]
        }
        return JsonResponse(data)


    elif request.method == 'PUT':
         # Parse the JSON data from the request body
        data = json.loads(request.body)
        print("Received data:", data)  # Debugging statement
        
        # Update invoice data
        invoice.date = data.get('date', invoice.date)
        invoice.cust_name = data.get('cust_name', invoice.cust_name)
        invoice.save()

    # Delete existing details
        invoice.details.all().delete()
        
        # Create new details
        new_details = []
        for detail_data in data.get('details', []):
            detail = InvoiceDetails.objects.create(
                invoice=invoice,
                description=detail_data.get('description'),
                quantity=detail_data.get('quantity'),
                unit_price=detail_data.get('unit_price'),
                price=detail_data.get('price')
            )
            new_details.append(detail)
            print("Created detail:", detail) 

        return JsonResponse({'message': 'Invoice and details updated successfully'})

    elif request.method == 'DELETE':
        invoice.delete()# Delete the invoice
        return JsonResponse({'message': 'Invoice deleted successfully'}, status=204)
