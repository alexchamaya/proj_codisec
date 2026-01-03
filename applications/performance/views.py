from django.shortcuts import render
from .models import Performance
from django.views.generic.list import ListView

# Create your views here.
class AssessmentListView(ListView):
    template_name = "performance/assessment_list.html"
    context_object_name = 'assessments'
    #paginate_by = 10

    def get_queryset(self):
        return Performance.objects.filter(type_performance='E', estado=True).order_by('-created_at')

class AgreementListView(ListView):
    template_name = "performance/agreement_list.html"
    context_object_name = 'agreements'
    #paginate_by = 10

    def get_queryset(self):
        return Performance.objects.filter(type_performance='A', estado=True).order_by('-created_at')

