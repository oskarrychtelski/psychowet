# Generated by Django 4.1 on 2022-09-03 09:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220903_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notatki',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]