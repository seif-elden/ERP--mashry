# Generated by Django 4.1.5 on 2023-01-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0017_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='emp_type',
            field=models.CharField(choices=[('تم التثبيت', 'تم التثبيت'), ('يتم التجربة', 'يتم التجربة')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('مؤنث', 'مؤنث'), ('مذكر', 'مذكر')], default='', max_length=20),
        ),
    ]
