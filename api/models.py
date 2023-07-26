from django.db import models
from django.contrib.auth.models import AbstractUser


class Prof(AbstractUser):


    profession = models.CharField(
        max_length=100, default="professeur ordinaire", blank=True, null=True
    )
    numero = models.CharField(
        max_length=15, verbose_name="numero de telephone", blank=True, null=True
    )

    profile = models.ImageField(
        upload_to="profile/", blank=True, null=True
    )

    adresse = models.CharField(
        max_length=3000, null=True, blank=True
    )



