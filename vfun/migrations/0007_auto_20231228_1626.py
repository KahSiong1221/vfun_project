# Generated by Django 3.2.23 on 2023-12-28 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vfun', '0006_auto_20231226_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='organizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organized_sessions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='session',
            name='players',
            field=models.ManyToManyField(blank=True, related_name='joined_sessions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sportshall',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sportshalls', to=settings.AUTH_USER_MODEL),
        ),
    ]
