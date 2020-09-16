# Generated by Django 3.1.1 on 2020-09-14 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("members", "0013_auto_20200913_1210"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="role",
            field=models.CharField(
                choices=[("Lead", "Lead"), ("Core", "Core"), ("Co-Lead", "Co-Lead")],
                max_length=255,
            ),
        ),
    ]