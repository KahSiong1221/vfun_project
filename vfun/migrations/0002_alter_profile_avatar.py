# Generated by Django 4.2.7 on 2023-11-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vfun", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="profile_images/default.png", upload_to="profile_images"
            ),
        ),
    ]