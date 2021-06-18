# Generated by Django 3.0.8 on 2021-03-20 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_life_employees_insurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='health_insurance',
            name='Maturity_Date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='life_childrens_insurance',
            name='Maturity_Date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='life_employees_insurance',
            name='Maturity_Date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='health_applications',
            name='App_Aadhar_Id',
            field=models.FileField(upload_to='Applications/Health/Documents'),
        ),
        migrations.AlterField(
            model_name='health_applications',
            name='Birth_Id',
            field=models.FileField(upload_to='Applications/Health/Documents'),
        ),
        migrations.AlterField(
            model_name='health_applications',
            name='Nom_Aadhar_Id',
            field=models.FileField(upload_to='Applications/Health/Documents'),
        ),
        migrations.AlterField(
            model_name='health_applications',
            name='image',
            field=models.ImageField(upload_to='Applications/Health/Images'),
        ),
        migrations.AlterField(
            model_name='health_insurance',
            name='App_Aadhar_Id',
            field=models.FileField(upload_to='Insurance/Health/Documents'),
        ),
        migrations.AlterField(
            model_name='health_insurance',
            name='Birth_Id',
            field=models.FileField(upload_to='Insurance/Health/Documents'),
        ),
        migrations.AlterField(
            model_name='health_insurance',
            name='Nom_Aadhar_Id',
            field=models.FileField(upload_to='Insurance/Health/Documents'),
        ),
        migrations.AlterField(
            model_name='health_insurance',
            name='Policy_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='health_insurance',
            name='image',
            field=models.ImageField(upload_to='Insurance/Health/Images'),
        ),
        migrations.AlterField(
            model_name='life_childrens_applications',
            name='Birth_Id',
            field=models.FileField(upload_to='Applications/Life_Childrens/Documents'),
        ),
        migrations.AlterField(
            model_name='life_childrens_applications',
            name='Nom_Aadhar_Id',
            field=models.FileField(upload_to='Applications/Life_Childrens/Documents'),
        ),
        migrations.AlterField(
            model_name='life_childrens_insurance',
            name='Birth_Id',
            field=models.FileField(upload_to='Insurance/Life_Childrens/Documents'),
        ),
        migrations.AlterField(
            model_name='life_childrens_insurance',
            name='Nom_Aadhar_Id',
            field=models.FileField(upload_to='Insurance/Life_Childrens/Documents'),
        ),
        migrations.AlterField(
            model_name='life_childrens_insurance',
            name='Policy_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='life_employees_applications',
            name='App_Aadhar_Id',
            field=models.FileField(upload_to='Applications/Life_Employees/Documents'),
        ),
        migrations.AlterField(
            model_name='life_employees_applications',
            name='Employement_Id',
            field=models.FileField(upload_to='Applications/Life_Employees/Documents'),
        ),
        migrations.AlterField(
            model_name='life_employees_applications',
            name='Nom_Aadhar_Id',
            field=models.FileField(upload_to='Applications/Life_Employees/Documents'),
        ),
        migrations.AlterField(
            model_name='life_employees_applications',
            name='image',
            field=models.ImageField(upload_to='Applications/Life_Employees/Images'),
        ),
        migrations.AlterField(
            model_name='life_employees_insurance',
            name='App_Aadhar_Id',
            field=models.FileField(upload_to='Insurance/Life_Employees/Documents'),
        ),
        migrations.AlterField(
            model_name='life_employees_insurance',
            name='Employement_Id',
            field=models.FileField(upload_to='Insurance/Life_Employees/Documents'),
        ),
        migrations.AlterField(
            model_name='life_employees_insurance',
            name='Nom_Aadhar_Id',
            field=models.FileField(upload_to='Insurance/Life_Employees/Documents'),
        ),
        migrations.AlterField(
            model_name='life_employees_insurance',
            name='Policy_Date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='life_employees_insurance',
            name='image',
            field=models.ImageField(upload_to='Insurance/Life_Employees/Images'),
        ),
    ]
