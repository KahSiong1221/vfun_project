# Generated by Django 3.2.23 on 2023-12-26 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vfun', '0003_auto_20231226_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['datetime']},
        ),
    ]
