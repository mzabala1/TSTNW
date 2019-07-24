from django.urls import path
from .views import opinion_view

app_name = "OpinionApp"

urlpatterns = [
        path('', opinion_view, name="Opinion"),
]
