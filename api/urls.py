from django.urls import path
from .views import horaireNext, userList


app_name = "api"


urlpatterns = [
    path('horaire/next', horaireNext, name="horaireNext"),
    path('profile/list', userList, name="userList"),
]