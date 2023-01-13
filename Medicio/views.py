from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from Medicio.forms.patient_form import PatientForm
from Medicio.models.patient import Patient


class PatientView(View):
    form_class = PatientForm
    initial = {'key': 'value'}
    template_name = 'index.html'
    context = {}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        context = {
            'form': self.form_class
        }
        return render(request, self.template_name, context)
