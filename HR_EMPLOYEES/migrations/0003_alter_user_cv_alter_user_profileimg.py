# Generated by Django 4.1.5 on 2023-01-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0002_management_jobtitle_department_department_management'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='CV',
            field=models.FileField(upload_to='images/uploads/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ProfileImg',
            field=models.ImageField(upload_to='images/uploads/'),
        ),
    ]