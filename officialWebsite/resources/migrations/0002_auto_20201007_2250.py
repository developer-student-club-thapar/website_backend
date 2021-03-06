# Generated by Django 3.1.1 on 2020-10-07 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resources", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="resource",
            name="description",
            field=models.TextField(default="Human", max_length=255),
        ),
        migrations.AddField(
            model_name="resource",
            name="docs",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="resource",
            name="headline_event",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="resource",
            name="image",
            field=models.ImageField(blank=True, upload_to="resource-images/"),
        ),
        migrations.AddField(
            model_name="resource",
            name="info",
            field=models.TextField(default="Human", max_length=255),
        ),
        migrations.AddField(
            model_name="resource",
            name="title",
            field=models.CharField(default="Human", max_length=255),
        ),
        migrations.AlterField(
            model_name="resource",
            name="link",
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="resource",
            name="name",
            field=models.CharField(default="Human", max_length=255),
        ),
    ]
