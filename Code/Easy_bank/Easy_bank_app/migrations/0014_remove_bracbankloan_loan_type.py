# Generated by Django 3.2.2 on 2021-08-22 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0013_bracbankloan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bracbankloan',
            name='loan_type',
        ),
    ]