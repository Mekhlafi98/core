from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


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
    name = models.CharField(
        _("الاسم"),
        null=True,
        blank=True,
        max_length=100,
    )
    dob = models.DateField(
        _("تاريخ الميلاد"),
        null=True,
        blank=True,
    )
    height = models.FloatField(
        _("الطول"),
        null=True,
        blank=True,
        max_length=100,
    )
    weight = models.FloatField(
        _("الوزن"),
        null=True,
        blank=True,
        max_length=100,
    )
    blood_types = models.CharField(
        _("فصيلة الدم"),
        max_length=3,
        null=True,
        blank=True,
        choices=BLOOD_TYPE,
    )
    allergy = models.CharField(
        _("حساسية من"),
        max_length=255,
        null=True,
        blank=True,
    )
    phone = models.CharField(
        _("رقم الهاتف"),
        null=True,
        blank=True,
        max_length=20,
    )
    address = models.CharField(
        _("العنوان"),
        null=True,
        blank=True,
        max_length=255,
    )
    city = models.CharField(
        _("المدينة"),
        null=True,
        blank=True,
        max_length=255,
    )
    country = models.CharField(
        _("الدولة"),
        null=True,
        blank=True,
        max_length=255,
    )
    created_at = models.DateTimeField(
        _("تاريخ الإنشاء"),
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        editable=False,
    )

    class Meta:
        verbose_name = _("المريض")
        verbose_name_plural = _("المرضى")

    def __str__(self) -> str:
        return self.name
