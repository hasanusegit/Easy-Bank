# Generated by Django 3.1.4 on 2021-04-26 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='loan_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
