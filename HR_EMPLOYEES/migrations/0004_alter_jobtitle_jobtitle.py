# Generated by Django 4.1.5 on 2023-01-24 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("HR_EMPLOYEES", "0003_alter_user_cv_alter_user_profileimg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobtitle",
            name="JobTitle",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
