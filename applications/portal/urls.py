from .views import PortalIndexView
from django.urls import path

urlpatterns = [
    path('', PortalIndexView.as_view(), name='portal_index'),
]