from django.db import models
from kristal.models import User

class ProfileCustomer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,null=True , blank=True)
    addres = models.CharField(max_length=50 , blank=True, null=True)
    name=models.CharField(max_length= 200)
    image=models.URLField()
   # ImageField(upload_to='photos/%y/%m/%d')
    categoryList=[('Keheilan','Keheilan'),('Seglawi','Seglawi')
    ,('Abeyan ','Abeyan '),
     ('Hamdani','Hamdani'),('Hadban','Hadban'),
    ]
    interests =models.CharField(max_length= 200,null=True,blank=True,choices=categoryList)
    def __str__(self):
        return str(self.user)

