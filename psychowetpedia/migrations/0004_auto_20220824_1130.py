# Generated by Django 4.1 on 2022-08-24 09:30

from django.db import migrations
import uuid

def gen_uuid_leki(apps, schema_editor):
    Leki = apps.get_model('psychowetpedia', 'Leki')
    for row in Leki.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])

def gen_uuid_zaburzenia(apps, schema_editor):
    Zaburzenia = apps.get_model('psychowetpedia', 'Zaburzenia')
    for row in Zaburzenia.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])

class Migration(migrations.Migration):

    dependencies = [
        ('psychowetpedia', '0003_leki_uuid_zaburzenia_uuid'),
    ]

    operations = [
        migrations.RunPython(gen_uuid_leki, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(gen_uuid_zaburzenia, reverse_code=migrations.RunPython.noop),
    ]
