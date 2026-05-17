from django.db import models


class SexChoices(models.TextChoices):
    MASCULIN = 'Masculin'
    FEMININ = 'Féminin'
