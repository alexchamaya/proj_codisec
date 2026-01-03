from .views import NormsListView
from django.urls import path

urlpatterns = [
    path('norms/', NormsListView.as_view(), name='norms_list'),
]
