from django.shortcuts import render
from django.views.generic import ListView
from .models import Plan

# Create your views here.

class PlanListView(ListView):
    template_name = "plan/plan_list.html"
    context_object_name = 'plans'
    #paginate_by = 10

    def get_queryset(self):
        return Plan.objects.all().order_by('-created_at')

