# Generated by Django 2.2.10 on 2020-05-15 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0006_event_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={"ordering": ["-date"]},
        ),
    ]
