# Generated by Django 4.2.2 on 2023-06-22 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="rest_full_details",
            field=models.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="rest_items",
            field=models.JSONField(null=True),
        ),
    ]