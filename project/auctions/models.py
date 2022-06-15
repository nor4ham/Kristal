from django.db import models
from horses.models import Horse
from customers.models import Customer

class auction(models.Model):
   horse =models.ForeignKey(Horse,on_delete=models.CASCADE,related_name='horses')
   upate_price=models.IntegerField()
   customer=models.ManyToManyField(Customer)
   date=models.DateField()
   accepted = models.BooleanField(default=False)
