# Generated by Django 4.1.3 on 2023-01-17 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Medicio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="A",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="C",
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
                ("name", models.CharField(max_length=30)),
                (
                    "a",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Medicio.a"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="B",
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
                ("name", models.CharField(max_length=30)),
                (
                    "a",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Medicio.a"
                    ),
                ),
            ],
        ),
    ]
