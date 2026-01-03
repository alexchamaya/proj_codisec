from .views import PlanListView
from django.urls import path

urlpatterns = [
    path('plan/', PlanListView.as_view(), name='plan_list'),
]
