from django.db import models
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _
from Medicio.models.patient import Patient


class Medication(models.Model):
    frequency_list = (
        ('OD', 'Once a day'),
        ('BDS', 'Twice daily'),
        ('T.I.D.', '3 times a day'),
        ('Q.I.D.', '4 times a day'),
        ('Q.Q.H.', 'Every 4 hours'),
        ('EOD', 'Every other day'),
        ('Q.N.', 'Every night'),
        ('Q.H.S.', 'Every night at bedtime'),
        ('Q.H.', 'Every hour'),
        ('P.R.N.', 'As needed'),
    )
    scientific_name = models.CharField(
        _("Scientific name"), null=True, blank=True, max_length=100)
    commercial_name = models.CharField(
        _("Commercial name"), null=True, blank=True, max_length=100)
    description = models.TextField(
        _("Description"), null=True, blank=True, max_length=1000)
    dosage = models.TextField(_("dosage"), null=True,
                              blank=True, max_length=100)
    frequency = models.CharField(
        _("frequency"), null=True, blank=True, max_length=10, choices=frequency_list)
    duration = models.CharField(
        _("duration"), null=True, blank=True, max_length=100)
    start_date = models.DateField(
        _("start_date"), null=True, blank=True, max_length=100)
    end_date = models.DateField(
        _("end_date"), null=True, blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.scientific_name
