# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2024-11-19 133035.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books


## PROGRA
from django.contrib import admin

from .models import bank_loan,bank_loanAdmin

admin.site.register(bank_loan,bank_loanAdmin)


class bank_loan(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    customer_name=models.CharField(max_length=22)
    bank_id=models.IntegerField()
    loan_amount=models.IntegerField()
    loan_id=models.IntegerField()

class bank_loanAdmin(admin.ModelAdmin):
        list_display=('customer_id','customer_name','bank_id','loan_amount','loan_id')



## OUTPUT

![alt text](<Screenshot 2024-11-16 114139.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
