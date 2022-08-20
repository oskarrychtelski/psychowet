from django.db import models
import uuid

# Create your models here.

class Zaburzenia(models.Model):
    nazwa = models.CharField(max_length=200, unique=True, primary_key=True)
    opis = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nazwa


class Leki(models.Model):
    nazwa = models.CharField(max_length=200, unique=True, primary_key=True)
    mechanizm = models.TextField(null=True, blank=True)
    opis = models.TextField(null=True, blank=True)
    przeciwwskazania = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nazwa


class Leczenie(models.Model):
    zaburzenie = models.ForeignKey('Zaburzenia', on_delete=models.CASCADE)
    lek = models.ForeignKey('Leki', on_delete=models.CASCADE)
    dawka_pies = models.CharField(max_length=200, null=True, blank=True)
    dawka_kot = models.CharField(max_length=200, null=True, blank=True)
    opis = models.TextField(null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return '{} ({})'.format(self.zaburzenie, self.lek)