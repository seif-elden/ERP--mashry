# Generated by Django 4.1.5 on 2023-01-30 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR_EMPLOYEES', '0024_remove_management_user_jobtitle_management_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bank_account_iban',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bank_account_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='paypal_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bank_account',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]