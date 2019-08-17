from rest_framework.serializers import ModelSerializer
from .models import Opinion


class OpinionSerializer(ModelSerializer):

    class Meta:
        model = Opinion
        fields = ('id', 'escritor', 'fecha', 'pre1', 'pre2', 'pre3')
        read_only_fields = ['id', 'escritor']
