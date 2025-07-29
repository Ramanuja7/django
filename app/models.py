from django.db import models
class student(models.Models):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
def _str_(self):
    return f"{self.name}-{self.rollno}"

 # Create your models here.
