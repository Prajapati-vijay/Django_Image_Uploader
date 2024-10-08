from django.db import models

# Create your models here.


class Student(models.Model):
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=80)
    Roll_No=models.IntegerField()

class Imagepload(models.Model):
    image=models.ImageField(upload_to='media/')
    name=models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.name