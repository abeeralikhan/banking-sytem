from django.db import models
# FUNDS TRANSFER APP MODELS

class Accounts(models.Model):
    accountTitle = models.CharField(max_length=20, blank=True)
    accountOpeningDate = models.DateField(blank=True)
    accountNo = models.CharField(max_length=20, blank=True)
    availableBalance = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    currency = models.CharField(max_length=5, default="PKR")
    IBAN = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, default="Active")

    def __str__(self):
        return self.accountTitle
