from .views import DnivehicularIndexView
from django.urls import path

urlpatterns = [
    path('', DnivehicularIndexView.as_view(), name='dnivehicular'),
]   