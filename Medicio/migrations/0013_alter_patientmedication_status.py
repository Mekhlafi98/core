# Generated by Django 4.1.3 on 2023-02-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Medicio", "0012_patient_created_by_alter_patientmedication_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientmedication",
            name="status",
            field=models.CharField(
                choices=[(0, "ليس بعد"), (1, "تم تناوله")],
                default=0,
                max_length=1,
                verbose_name="الحالة",
            ),
        ),
    ]
