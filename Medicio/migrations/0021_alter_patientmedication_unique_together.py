# Generated by Django 4.1.3 on 2023-02-04 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Medicio", "0020_alter_medication_dose"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="patientmedication",
            unique_together=set(),
        ),
    ]
