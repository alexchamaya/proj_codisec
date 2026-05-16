from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PortalIndexView(TemplateView):
    template_name = 'portal/index.html'