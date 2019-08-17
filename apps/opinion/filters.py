import django_filters
from .models import Opinion


class OpinionFilter(django_filters.FilterSet):

    class Meta:
        model = Opinion
        fields = ('escritor', 'pre3')
