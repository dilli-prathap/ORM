from django.contrib import admin

from .models import bank_loan,bank_loanAdmin

admin.site.register(bank_loan,bank_loanAdmin)