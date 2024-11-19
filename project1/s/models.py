from django.db import models
from django.contrib import admin

class bank_loan(models.Model):
    customer_id=models.IntegerField(primary_key=True)
    customer_name=models.CharField(max_length=22)
    bank_id=models.IntegerField()
    loan_amount=models.IntegerField()
    loan_id=models.IntegerField()

class bank_loanAdmin(admin.ModelAdmin):
        list_display=('customer_id','customer_name','bank_id','loan_amount','loan_id')
