from rest_framework.serializers import ModelSerializer
from .models import HoraireAlarm, Prof


class HoraireSerializer(ModelSerializer):
    class Meta:
        model = HoraireAlarm
        fields = [
            'id', 'dateCreation', 'createur', 'modifiable', 'date', 'description'
        ]


class ProfDetailSerializer(ModelSerializer):

    class Meta:
        model = Prof
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'numero', 'adresse', 'profession',
            'profile'
        ]

