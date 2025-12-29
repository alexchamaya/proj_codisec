from .views import ActivitiesView, HomeListView
from django.urls import path

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('activities/', ActivitiesView.as_view(), name='activities'),
]