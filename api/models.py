from django.db import models
from django.contrib.auth.models import AbstractUser


class Prof(AbstractUser):
    genre = models.CharField(max_length=7, choices=(
        ("homme", "homme"),
        ('femme', 'femme')
    ))

    profile = models.ImageField(
        upload_to="profile/", blank=True, null=True, default="defaul.jpg"
    )

    profession = models.CharField(
        max_length=100, default="professeur ordinaire", blank=True, null=True
    )
    numero = models.CharField(
        max_length=15, verbose_name="numero de telephone", blank=True, null=True
    )

    adresse = models.CharField(
        max_length=3000, null=True, blank=True
    )

    def __str__(self):
        return f"{self.first_name}|{self.last_name}|{self.genre}|{self.profile.url}|{self.profession}|{self.adresse}"


class HoraireAlarm(models.Model):
    dateCreation = models.DateTimeField(verbose_name="date de creation", auto_now=True)
    createur = models.ForeignKey(Prof, on_delete=models.CASCADE)

    modifiable = models.BooleanField(default=False)

    date = models.DateTimeField()

    description = models.CharField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return f"prevu pour {self.date}, creer par {self.createur.first_name}"

    class Meta:
        ordering = ("-dateCreation",)
