from django.urls import path
from .views import opinion_view, opiniones_list

app_name = "OpinionApp"

urlpatterns = [
        path('', opinion_view, name="Opinion"),
        path('opiniones', opiniones_list, name='Opiniones'),
]
