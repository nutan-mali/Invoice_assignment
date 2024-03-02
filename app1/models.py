from django.db import models

# Create your models here.
class Invoice(models.Model):
    date = models.DateField()
    cust_name = models.CharField(max_length=50)

    def __str__(self):
        return self.cust_name
    
class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details',on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description