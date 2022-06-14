from django.db import models
from kristal.models import User

class ProfileSeller(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,null=True , blank=True)
    addres = models.CharField(max_length=50 , blank=True, null=True)
    name=models.CharField(max_length= 200)
    image=models.URLField()
    def __str__(self):
        return str(self.user)