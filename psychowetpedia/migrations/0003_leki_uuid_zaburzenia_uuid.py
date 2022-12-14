# Generated by Django 4.1 on 2022-08-24 09:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('psychowetpedia', '0002_zaburzenia_spec_gat'),
    ]

    operations = [
        migrations.AddField(
            model_name='leki',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
        migrations.AddField(
            model_name='zaburzenia',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, null=True),
        ),
    ]
