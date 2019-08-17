from django.urls import path
from .views import opinion_view, opiniones_list, OpinionesFullList, OpinionesRudView

app_name = "OpinionApp"

urlpatterns = [
        path('', opinion_view, name="Opinion"),
        path('opiniones', opiniones_list, name='Opiniones'),
        path('api/opiniones/', OpinionesFullList.as_view(), name='rest-opiniones-list'),
        path('api/opiniones/<pk>/', OpinionesRudView.as_view(), name='rest-opiniones-rud'),
]
