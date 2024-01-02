from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(null=True, max_length=20)


class SportsHall(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    location = models.PointField()
    courts = models.IntegerField(default=1)
    phone_no = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, related_name='sportshalls', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Session(models.Model):
    LEVELS = [
        ("ALL", "All level"),
        ("BEG", "Beginner"),
        ("INT", "Intermediate"),
        ("ADV", "Advanced"),
        ("EXP", "Expert"),
    ]

    GENDERS = [
        ("MIX", "Mixed"),
        ("MEN", "Men"),
        ("WOM", "Women"),
    ]

    hall = models.ForeignKey(SportsHall, related_name='sessions', on_delete=models.CASCADE)
    organizer = models.ForeignKey(User, related_name='organized_sessions', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    duration_min = models.IntegerField()
    capacity = models.IntegerField()
    level = models.CharField(max_length=3, choices=LEVELS, default=LEVELS[0][0])
    gender = models.CharField(max_length=3, choices=GENDERS, default=GENDERS[0][0])
    players = models.ManyToManyField(User, related_name="joined_sessions", blank=True)
    price = models.FloatField(default=0)

    class Meta:
        ordering = ['datetime']

    def __str__(self):
        return self.hall.name + ' | ' + self.datetime.strftime("%d-%m-%Y %H:%M")
