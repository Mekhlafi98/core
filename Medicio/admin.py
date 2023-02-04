from django.contrib import admin
from .models.medication import Medication, PatientMedication
from .models.patient import Patient
from django.contrib import messages
from django.utils.translation import ngettext
from django.utils.translation import gettext_lazy as _


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_per_page = 10  # No of records per page
    list_display = (
        "name",
        "dob",
        "height",
        "weight",
        "blood_types",
        "allergy",
        "phone",
        "address",
    )
    fieldsets = (
        (_("الدواء"), {
            'fields': (
                ('name', 'dob', 'height',),
                ('weight', 'blood_types', 'allergy',),
                ('phone', 'address', 'city', 'country',),
            ),
            'classes': ('wide', 'extrapretty'),
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(created_by=request.user)


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    search_fields = [
        'scientific_name',
    ]
    list_per_page = 10  # No of records per page
    list_display = (
        "scientific_name",
        "commercial_name",
        "usage",
        "get_dose",
        "quantity",
        "frequency",
        "duration",
        "start_date",
        "end_date",
    )

    def get_dose(self, obj):
        return f"{obj.dose} حبة"
    get_dose.short_description = "الجرعة"

    def show_remaining(self, obj):
        from django.db.models import Avg
        result = Medication.objects.filter(id=obj).aggregate(Avg("grade"))
        return result["grade__avg"]

    def make_taken(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)


@admin.register(PatientMedication)
class PatientMedicationAdmin(admin.ModelAdmin):
    radio_fields = {"status": admin.VERTICAL}
    fieldsets = (
        (_("ربط المريض بالدواء"), {
            'fields': (('patient', 'medication', 'status'),),
            'classes': ('wide', 'extrapretty'),
        }),
    )
    autocomplete_fields = [
        'patient',
        'medication',
        'user',
    ]

    list_display = (
        "patient",
        "medication",
        "user",
        "status",
        "updated_at",
    )
    list_filter = (
        'status',
        "updated_at",
    )
    search_fields = [
        "patient__name",
        "medication__commercial_name",
    ]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs if request.user.is_superuser else qs.filter(user=request.user)

    actions = [
        'apply_taken',
    ]

    def apply_taken(self, request, queryset):
        queryset.update(status="1")
    apply_taken.short_description = 'تم تناولها'

    def save_model(self, request, instance, form, change):
        user = request.user
        instance = form.save(commit=False)
        if instance.status == "1":
            obj = Medication.objects.get(id=instance.medication.id)
            if obj.quantity < obj.dose:
                self.message_user(request, ngettext(
                    '%d  لا توجد كمية كافية من الدواء لأخذ الجرعة',
                    '%d  لا توجد كمية كافية من الدواء لأخذ الجرعة',
                    obj.id,
                ) % obj.id, messages.ERROR)
            else:
                new_quantity = float(obj.quantity)-obj.dose
                obj.quantity = new_quantity
                obj.save()
        if not change or not instance.user:
            instance.user = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance
