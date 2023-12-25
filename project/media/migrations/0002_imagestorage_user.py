# Generated by Django 4.2.4 on 2023-12-25 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagestorage',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.expressions.Case, to=settings.AUTH_USER_MODEL),
        ),
    ]
