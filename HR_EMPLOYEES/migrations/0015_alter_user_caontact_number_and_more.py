# Generated by Django 4.1.5 on 2023-01-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0014_remove_daysofftypes_leave_en'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='caontact_number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='emergancy_contact',
            field=models.CharField(max_length=12, null=True),
        ),
    ]