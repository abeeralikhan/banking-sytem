from django.db import models
from django.contrib.auth.models import User
from fundsTransfer.models import Accounts

# BANK STATEMENT MODELS

class TransactionDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    account_no = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    tr_date = models.DateField(auto_now_add=False)
    description =  models.CharField(max_length=50)
    debit = models.DecimalField(max_digits=1000, decimal_places=2)
    credit = models.DecimalField(max_digits=1000, decimal_places=2)
    available_balance = models.DecimalField(max_digits=1000, decimal_places=2)

