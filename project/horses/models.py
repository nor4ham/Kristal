from django.db import models
from sellers.models import Seller as Profileseller
class Horse(models.Model):
#    seller =User.objects.get(is_seller=True)
    name=models.CharField(max_length= 200)
    image=models.URLField()
    history=models.TextField(blank=True)
    price=models.IntegerField(default=0)
    categoryList=[('Keheilan','Keheilan'),('Seglawi','Seglawi')
    ,('Abeyan ','Abeyan '),
     ('Hamdani','Hamdani'),('Hadban','Hadban'),
    ]
    pedigree =models.CharField(max_length= 200,null=True,blank=True,choices=categoryList)
    seller =models.ForeignKey(Profileseller,on_delete=models.CASCADE,related_name='horses')
    create_daate=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.name)

class Comment(models.Model):
    body=models.TextField(verbose_name='')
    comment_daate=models.DateTimeField(auto_now=True)
    horse =models.ForeignKey(Horse,on_delete=models.CASCADE,related_name='comments_horse')
    def __str__(self):
        return self.body
    class Meta:   
        ordering=['-comment_daate']
