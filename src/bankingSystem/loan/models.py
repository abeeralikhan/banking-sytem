from django.db import models

# LOAN APP MODELS
loan_types = [
    ('ST', 'Short-term'),
    ('IT', 'Intermediate-term'),
    ('LT', 'Long-term'),
]

maturities = [
    ('ONE_YEAR', '1'),
    ('FIVE_YEARS', '5'),
    ('SEVEN_YEARS', '7'),
    ('TEN_YEARS', '10'),
]

repayment_schedules = [
    ('ML', 'Monthly'),
    ('SA', 'Semi-annual')
]

loan_amounts = [
    ('HUNDRED_K', '100000'),
    ('FIVE_HUNDRED_K', '500000'),
    ('SEVEN_HUNDRED_K', '700000'),
    ('ONE_MILLION', '1000000'),
]
class Loan(models.Model):
    name = models.CharField(max_length=20)
    cnic = models.CharField(max_length=14)
    phone = models.CharField(max_length=20)
    monthly_income = models.DecimalField(max_digits=6, decimal_places=2)
    loan_type = models.CharField(max_length=20, choices=loan_types, default='Short-term')
    maturity = models.CharField(max_length=20, choices=maturities, default='1')
    repayment_schedule = models.CharField(max_length=20, choices=repayment_schedules, default='Monthly')
    loan_amount = models.CharField(max_length=20, choices=loan_amounts, default='100000')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cnic + '_' + self.loan_type + '_' + self.loan_amount + '_' + self.datetime