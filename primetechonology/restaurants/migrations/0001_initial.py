# Generated by Django 4.2.2 on 2023-06-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rest_id", models.IntegerField()),
                ("rest_name", models.CharField(max_length=100)),
                ("rest_location", models.CharField(max_length=100)),
                ("rest_items", models.JSONField()),
                ("rest_lat_long", models.CharField(max_length=100)),
                ("rest_full_details", models.JSONField()),
            ],
        ),
    ]
