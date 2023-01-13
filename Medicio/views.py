from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')

# class MainView(View):
#     def get(self, request, *args, **kwargs):
#         return JsonResponse()
