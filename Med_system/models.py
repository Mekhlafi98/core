from django.db import models

from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _


class Common(models.Model):
    name = models.CharField(_("اسم الموظف"), max_length=255)
    max_debit = models.PositiveBigIntegerField(
        _("سقف المديونية"),)

    class Meta:
        abstract = True


class Employee(Common):
    def __str__(self) -> str:
        return self.name


class Customer(Common):
    def __str__(self) -> str:
        return self.name


class Currency(models.Model):
    CURRENCY_TYPES = [
        ('1', 'محلي'),
        ('2', 'أجنبي'),
    ]
    name = models.CharField(_("اسم العملة"), max_length=255)
    type = models.CharField(
        _("نوع العملة"), max_length=2, choices=CURRENCY_TYPES)
    exchange = models.FloatField(_("سعر الصرف"), default=0.0)


class Master(models.Model):
    OPERATION_TYPES = [
        ('1', 'سلف'),
        ('2', 'تسديد سلف'),
    ]

    amount = models.FloatField(_("المبلغ"))
    currency = models.ForeignKey(
        Currency,  choices=OPERATION_TYPES, on_delete=models.CASCADE)


class DetailQueryset(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        lookups = Q(account_type=query)
        return self.filter(lookups)


class DetailManager(models.Manager):
    def get_queryset(self):
        return DetailQueryset(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

    # def search(self, query=None):
    #     if query is None or query == "":
    #         return self.get_queryset().none()  # []
    #     lookups = Q(account_type=query)
    #     return self.get_queryset().filter(lookups)


class Detail(models.Model):
    OPERATION_TYPES = [
        ('1', 'عميل'),
        ('2', 'موظف'),
    ]
    account_type = models.CharField(
        _("نوع الحساب"), max_length=10, choices=OPERATION_TYPES)

    objects = models.Manager()
    DetailManager = DetailManager()


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


class Note(models.Model):
    title = models.TextField(
        _("Title"), null=True, blank=True, max_length=255)
    body = models.TextField(
        _("Body"), null=True, blank=True, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
