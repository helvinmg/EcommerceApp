from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    lang=[('Eng','English'),('Hin','Hindi')]
    cname=models.CharField(max_length=30)
    cdescription=models.CharField(max_length=250)
    creator=models.CharField(max_length=40)
    clang=models.CharField(choices=lang,max_length=40)
    cprice=models.IntegerField()
    cimage=models.ImageField(upload_to="images/",default="images/noimage.png")
    
    def __str__(self):
        return self.cname
   
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    quantity=models.IntegerField()

class MyOrders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ordername=models.CharField(max_length=35,default="NA")
    #orderdate=models.DateField(null=True)
    amount=models.IntegerField()
    status=models.CharField(max_length=35,default="Failed")