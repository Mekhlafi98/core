# Generated by Django 4.1.3 on 2023-02-04 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Medicio", "0006_publication_article"),
    ]

    operations = [
        migrations.CreateModel(
            name="PatientMedication",
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
                ("updated_by", models.CharField(max_length=16, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="customer",
            name="person",
        ),
        migrations.RemoveField(
            model_name="customera",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="customerb",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="person",
        ),
        migrations.RemoveField(
            model_name="medication",
            name="patient",
        ),
        migrations.DeleteModel(
            name="Article",
        ),
        migrations.DeleteModel(
            name="Customer",
        ),
        migrations.DeleteModel(
            name="CustomerA",
        ),
        migrations.DeleteModel(
            name="CustomerB",
        ),
        migrations.DeleteModel(
            name="Employee",
        ),
        migrations.DeleteModel(
            name="Person",
        ),
        migrations.DeleteModel(
            name="Publication",
        ),
        migrations.AddField(
            model_name="patientmedication",
            name="medication",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Medicio.medication"
            ),
        ),
        migrations.AddField(
            model_name="patientmedication",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Medicio.patient"
            ),
        ),
        migrations.AddField(
            model_name="medication",
            name="patients",
            field=models.ManyToManyField(
                through="Medicio.PatientMedication", to="Medicio.patient"
            ),
        ),
    ]
