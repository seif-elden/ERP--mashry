# Generated by Django 4.1.5 on 2023-01-31 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0029_alter_weakly_leave_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave_request',
            name='accepted',
            field=models.BooleanField(null=True),
        ),
    ]