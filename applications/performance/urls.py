from .views import AssessmentListView, AgreementListView
from django.urls import path

urlpatterns = [
    path('assessments/', AssessmentListView.as_view(), name='assessment_list'),
    path('agreements/', AgreementListView.as_view(), name='agreement_list'),
]
