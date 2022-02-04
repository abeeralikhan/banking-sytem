# Generated by Django 4.0.1 on 2022-02-04 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cnic', models.CharField(max_length=14)),
                ('phone', models.CharField(max_length=20)),
                ('monthly_income', models.DecimalField(decimal_places=2, max_digits=6)),
                ('loan_type', models.CharField(choices=[('ST', 'Short-term'), ('IT', 'Intermediate-term'), ('LT', 'Long-term')], default='Short-term', max_length=20)),
                ('maturity', models.CharField(choices=[('ONE_YEAR', '1'), ('FIVE_YEARS', '5'), ('SEVEN_YEARS', '7'), ('TEN_YEARS', '10')], default='1', max_length=20)),
                ('repayment_schedule', models.CharField(choices=[('ML', 'Monthly'), ('SA', 'Semi-annual')], default='Monthly', max_length=20)),
                ('loan_amount', models.CharField(choices=[('HUNDRED_K', '100000'), ('FIVE_HUNDRED_K', '500000'), ('SEVEN_HUNDRED_K', '700000'), ('ONE_MILLION', '1000000')], default='100000', max_length=20)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
