from django.db import models
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from Medicio.models.patient import Patient
from django.contrib.auth import get_user_model


class Medication(models.Model):
    FREQUENCY_LIST = (
        ('OD', _("مرة باليوم")),
        ('BDS', _("مرتين باليوم")),
        ('T.I.D.', _("ثلاث مرات باليوم")),
        ('Q.I.D.', _('أربعة مرات في اليوم')),
        ('Q.Q.H.', _('كل أربع ساعات')),
        ('EOD', _('مرة كل يومين')),
        ('Q.N.', _('كل ليلة')),
        ('Q.H.S.', _('عند النوم')),
        ('Q.H.', _('كل ساعة')),
        ('P.R.N.', _('وقت الحاجة')),
    )
    MEDICINE_TYPES = (
        ('tablets', _("حبوب")),
        ('injection', _("حُقن")),
        ('syrup', _("شراب")),
    )
    scientific_name = models.CharField(
        _("الاسم العلمي"),
        null=True,
        blank=True,
        max_length=100
    )
    commercial_name = models.CharField(
        _("الاسم التجاري"),
        null=True,
        blank=True,
        max_length=100,
    )
    usage = models.TextField(
        _("الاستخدام"),
        null=True,
        blank=True,
        max_length=100,
    )
    quantity = models.PositiveIntegerField(
        _("العبوة"),
        null=False,
        blank=False,
    )
    frequency = models.CharField(
        _("التكرار"),
        null=True,
        blank=True,
        max_length=10,
        choices=FREQUENCY_LIST,
    )
    duration = models.CharField(
        _("الفترة"),
        null=True,
        blank=True,
        max_length=100,
    )
    dose = models.FloatField(
        _("الجرعة"),
        null=False,
        blank=False,
    )
    start_date = models.DateField(
        _("تاريخ البداية"),
        null=True,
        blank=True,
        max_length=100,
    )
    end_date = models.DateField(
        _("تاريخ النهاية"),
        null=True,
        blank=True,
        max_length=100,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ النهاية"),
    )
    medicine_type = models.CharField(
        verbose_name=_("نوع الدواء"),
        choices=MEDICINE_TYPES,
        default="tablets",
        max_length=15,
    )
    patients = models.ManyToManyField(
        Patient,
        through='PatientMedication',
        verbose_name=_("المريض"),
    )

    class Meta:
        verbose_name = _("الأدوية")
        verbose_name_plural = _("الأدوية")

    def __str__(self) -> str:
        return self.scientific_name


class PatientMedication(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        verbose_name=_("المريض")
    )
    medication = models.ForeignKey(
        Medication,
        on_delete=models.CASCADE,
        verbose_name=_("الدواء"),
    )
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        editable=False,
    )
    status = models.CharField(
        choices=(
            ("0", _('ليس بعد')),
            ("1", _('تم تناوله')),
        ),
        default="0",
        verbose_name=_("الحالة"),
        max_length=1,
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("تاريخ التحديث"),
    )

    def __str__(self) -> str:
        return f"{self.patient.name} - {self.medication.commercial_name}"

    class Meta:
        verbose_name = _("الاستخدام")
        verbose_name_plural = _("الاستخدامات")
        # unique_together = ('patient', 'medication',)
