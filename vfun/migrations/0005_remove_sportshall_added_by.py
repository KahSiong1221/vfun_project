# Generated by Django 4.2.7 on 2023-11-12 16:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vfun", "0004_remove_profile_bio_profile_phone_no_sportshall"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sportshall",
            name="added_by",
        ),
    ]