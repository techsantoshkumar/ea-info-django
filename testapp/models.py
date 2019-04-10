from django.db import models

# Create your models here.

# entaty class to create table

class Employee(models.Model):

    emp_name=models.CharField(max_length=1000)
    emp_email=models.EmailField(unique=True)
    emp_address=models.CharField(max_length=250)


    class Meta:
        db_table='employee'

class College(models.Model):
    clg_id=models.CharField(primary_key=True,max_length=200)
    clg_name=models.CharField(max_length=100)

