# Generated by Django 4.2.4 on 2023-11-29 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0002_region_delete_redion"),
    ]

    operations = [
        migrations.CreateModel(
            name="crime",
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
                ("district", models.CharField(max_length=200)),
                ("murder", models.IntegerField()),
                ("theft", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="Region",
        ),
    ]
