from django.shortcuts import render
from django.views.generic.list import ListView
from applications.legal.models import Norms

# Create your views here.
class NormsListView(ListView):
    template_name = "legal/norms_list.html"
    context_object_name = 'norms'
    #paginate_by = 10

    def get_queryset(self):
        return Norms.objects.all().order_by('-created_at')