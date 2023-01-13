from django.db import models

from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _


class Patient(models.Model):
    BLOOD_TYPE = [
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    name = models.CharField(_("Full Name"), null=True,
                            blank=True, max_length=100)
    dob = models.DateField(_("Date of birth"), null=True, blank=True)
    height = models.FloatField(
        _("Height"), null=True, blank=True, max_length=100)
    weight = models.FloatField(
        _("weight"), null=True, blank=True, max_length=100)
    blood_types = models.CharField(
        _("Blood Types"), null=True, blank=True, max_length=3)
    allergy = models.CharField(_("Allergy"), max_length=255)
    phone = models.CharField(_("Phone"), null=True, blank=True, max_length=20)
    address = models.CharField(
        _("Address"), null=True, blank=True, max_length=255)
    city = models.CharField(_("city"), null=True, blank=True, max_length=255)
    country = models.CharField(
        _("country"), null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
