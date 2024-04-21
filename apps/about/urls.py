from django.urls import path
from apps.about.views import index

urlpatterns = [
    path('', index, name='404'),
]
