# Generated by Django 4.1.5 on 2023-01-28 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0015_alter_user_caontact_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female')], default=' ', max_length=4),
        ),
    ]
