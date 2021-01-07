from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    course = models.CharField(max_length=80)


class Person(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    password = models.CharField(max_length=70)

