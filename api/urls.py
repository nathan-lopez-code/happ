from django.urls import path
from .views import horaireNext


app_name = "api"


urlpatterns = [
    path('horaire/next', horaireNext, name="horaireNext")
]