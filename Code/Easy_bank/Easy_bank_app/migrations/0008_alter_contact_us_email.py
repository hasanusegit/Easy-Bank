# Generated by Django 3.2.2 on 2021-06-03 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0007_contact_us_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='email',
            field=models.EmailField(max_length=500),
        ),
    ]
