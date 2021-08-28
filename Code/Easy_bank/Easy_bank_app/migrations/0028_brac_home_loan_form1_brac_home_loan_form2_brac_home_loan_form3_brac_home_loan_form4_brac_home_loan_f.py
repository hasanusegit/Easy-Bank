# Generated by Django 3.2.2 on 2021-08-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Easy_bank_app', '0027_brac_credit_card_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='brac_home_loan_form1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicants_name', models.CharField(max_length=250)),
                ('applicants_full_name', models.CharField(max_length=200)),
                ('applicants_father_name', models.CharField(max_length=200)),
                ('applicants_mother_name', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('contatct_no', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('nid', models.CharField(max_length=100)),
                ('loan_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='brac_home_loan_form2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('p_address', models.CharField(max_length=200)),
                ('second_contact_no', models.CharField(max_length=100)),
                ('second_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='brac_home_loan_form3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(max_length=100)),
                ('floor_size', models.CharField(max_length=100)),
                ('flat_no', models.CharField(max_length=100)),
                ('nationality_2', models.CharField(max_length=100)),
                ('utility', models.CharField(max_length=100)),
                ('expected_possesion', models.CharField(max_length=100)),
                ('date_expected', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='brac_home_loan_form4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_area', models.CharField(max_length=100)),
                ('loan_requested', models.CharField(max_length=100)),
                ('balance_amount', models.CharField(max_length=100)),
                ('payment_source', models.CharField(max_length=100)),
                ('property_selected', models.CharField(max_length=100)),
                ('contact_2', models.CharField(max_length=100)),
                ('email_3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='brac_home_loan_form5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=100)),
                ('designation_department', models.CharField(max_length=100)),
                ('office_address', models.CharField(max_length=200)),
                ('allowness', models.CharField(max_length=100, null=True)),
                ('additional_income', models.CharField(max_length=100, null=True)),
                ('salary_total', models.CharField(max_length=100, null=True)),
                ('office_no', models.CharField(max_length=100)),
            ],
        ),
    ]
