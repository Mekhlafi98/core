from django import forms
from Medicio.models.patient import Patient
from dal import autocomplete


class PatientForm(forms.ModelForm):
    """
    This is the form to register a patient
    it takes all the fields in the model
    """

    class Meta:
        model = Patient
        fields = "__all__"
        # widgets = {
        #     'allergy': autocomplete.ModelSelect2Multiple(
        #         url='allergy-autocomplete',
        #     )
        # }
