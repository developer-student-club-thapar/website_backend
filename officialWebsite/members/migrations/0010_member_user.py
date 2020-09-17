# Generated by Django 2.2.8 on 2019-12-24 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("members", "0009_auto_20191224_2126"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="user",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
