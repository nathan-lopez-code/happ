from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Prof


class ProfCreationForm(UserCreationForm):
    class Meta:
        model = Prof
        fields = ('profession', 'numero', 'profile', 'adresse')


class ProfChangeForm(UserChangeForm):
    class Meta:
        model = Prof
        fields = ('profession', 'numero', 'profile', 'adresse')
