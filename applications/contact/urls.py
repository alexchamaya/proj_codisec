from django.urls import path
from .views import Contact_view

urlpatterns = [
    path('', Contact_view, name='contact'),
]
