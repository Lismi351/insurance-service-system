# Generated by Django 3.0.8 on 2021-03-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Health_Applications',
            fields=[
                ('Appl_Id', models.TextField(max_length=12, primary_key=True, serialize=False)),
                ('Category', models.CharField(max_length=10)),
                ('App_Name', models.CharField(max_length=50)),
                ('App_Father', models.CharField(max_length=50)),
                ('App_Mother', models.CharField(max_length=50)),
                ('App_DOB', models.DateField()),
                ('App_Gender', models.CharField(max_length=10)),
                ('App_Qual', models.CharField(max_length=10)),
                ('App_Mobile', models.CharField(max_length=15)),
                ('App_Aadhar', models.CharField(max_length=20)),
                ('App_Blood', models.CharField(max_length=5)),
                ('App_Email', models.CharField(max_length=50)),
                ('Addr1', models.CharField(max_length=50)),
                ('Addr2', models.CharField(max_length=50)),
                ('Addr3', models.CharField(max_length=50)),
                ('Pin', models.CharField(max_length=15)),
                ('Nom_Name', models.CharField(max_length=50)),
                ('Nom_DOB', models.DateField()),
                ('Relation', models.CharField(max_length=15)),
                ('Nom_Gender', models.CharField(max_length=10)),
                ('Nom_Aadhar', models.CharField(max_length=20)),
                ('Nom_Mobile', models.CharField(max_length=15)),
                ('Nom_Email', models.CharField(max_length=50)),
                ('Bank_Account', models.CharField(max_length=50)),
                ('Bank_Name', models.CharField(max_length=20)),
                ('Account_Number', models.CharField(max_length=50)),
                ('IFSC', models.CharField(max_length=50)),
                ('Branch', models.CharField(max_length=50)),
                ('Scheme', models.CharField(max_length=10)),
                ('Scheme_Amount', models.CharField(max_length=10)),
                ('App_Aadhar_Id', models.FileField(upload_to='Health/Documents')),
                ('Nom_Aadhar_Id', models.FileField(upload_to='Health/Documents')),
                ('Birth_Id', models.FileField(upload_to='Health/Documents')),
                ('image', models.ImageField(upload_to='Health/Images')),
                ('Payment_Card', models.CharField(max_length=20)),
                ('Name_Card', models.CharField(max_length=50)),
                ('Paid_Amount', models.CharField(max_length=10)),
                ('App_Status', models.CharField(default='Submitted', max_length=20)),
                ('Now_Date', models.DateField(auto_now=True)),
            ],
        ),
    ]
