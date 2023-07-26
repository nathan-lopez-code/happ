from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Prof
from .forms import ProfChangeForm, ProfCreationForm
from django.utils.translation import gettext_lazy as _


class ProfAdmin(UserAdmin):
    add_form = ProfCreationForm
    form = ProfChangeForm

    model = Prof
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'profile', 'numero')}),
        (_('others information'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Prof, ProfAdmin)
