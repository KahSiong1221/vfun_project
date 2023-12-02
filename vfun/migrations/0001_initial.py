# Generated by Django 3.2.23 on 2023-12-02 20:57

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SportsHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('courts', models.IntegerField(default=1)),
                ('phone_no', models.CharField(max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vfun.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('duration_min', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('level', models.CharField(choices=[('ALL', 'All level'), ('BEG', 'Beginner'), ('INT', 'Intermediate'), ('ADV', 'Advanced'), ('EXP', 'Expert')], default='ALL', max_length=3)),
                ('price', models.FloatField(default=0)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vfun.sportshall')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vfun.profile')),
                ('players', models.ManyToManyField(related_name='vfun_session_players', to='vfun.Profile')),
            ],
        ),
    ]
