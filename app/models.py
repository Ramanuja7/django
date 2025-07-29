from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100)

    rollno=models.IntegerField()
#def __str__(self):
   # return f"{self.name}-{self.rollno}"
class Details(models.Model):
    phonenumber=models.IntegerField(max_length=10)
    email=models.CharField(max_length=100)
def __str__(self):
    return f"{self.name}-{self.rollno}-{self.phonenumber}-{self.email}"



 # Create your models here.
