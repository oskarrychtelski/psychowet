from django.contrib import admin
from .models import Zaburzenia, Leki, Leczenie

admin.site.register(Zaburzenia)
admin.site.register(Leki)
admin.site.register(Leczenie)

