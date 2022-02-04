from dataclasses import field
from django.forms import ModelForm
from .models import Loan
class LoanForm(ModelForm):
    class Meta:
        model = Loan
        fields = ['name', 'cnic', 'phone', 'monthly_income', 'loan_type', 'maturity', 'repayment_schedule', 'loan_amount']