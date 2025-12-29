from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from applications.core.models import Miembros
# Create your views here.

# class HomeView(TemplateView):
#     template_name = "core/home.html"

class HomeListView(ListView):
    template_name = "core/home.html"
    context_object_name = 'miembros'
    #paginate_by = 10

    def get_queryset(self):
        return Miembros.objects.filter(estado=True).order_by('created_at')

class ActivitiesView(TemplateView):
    template_name = "core/activities.html"
