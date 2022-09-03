from django.db import models
from django.conf import settings
import uuid


class Notatki(models.Model):
    imie_zwierzecia = models.CharField(max_length=200, null=True, blank=True)
    zaburzenie = models.ForeignKey('psychowetpedia.Zaburzenia', on_delete=models.PROTECT)
    lek = models.ForeignKey('psychowetpedia.Leki', on_delete=models.PROTECT)
    opis = models.TextField(null=True, blank=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    # uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
