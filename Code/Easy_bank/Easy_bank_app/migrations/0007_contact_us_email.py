# Generated by Django 3.2.2 on 2021-05-24 15:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0006_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]
