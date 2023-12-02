from django.contrib.gis.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    phone_no = models.CharField(null=True, max_length=20)

    def __str__(self):
        return self.user.username


class SportsHall(models.Model):
    hall_name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    location = models.PointField()
    courts = models.IntegerField(default=1)
    phone_no = models.CharField(max_length=20)
    created_by = models.ForeignKey(Profile, on_delete=models.PROTECT)

    def __str__(self):
        return self.hall_name


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

    hall = models.ForeignKey(SportsHall, on_delete=models.CASCADE)
    organizer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    duration_min = models.IntegerField()
    capacity = models.IntegerField()
    level = models.CharField(max_length=3, choices=LEVELS, default=LEVELS[0][0])
    gender = models.CharField(max_length=3, choices=GENDERS, default=GENDERS[0][0])
    players = models.ManyToManyField(Profile, related_name="%(app_label)s_%(class)s_players")
    price = models.FloatField(default=0)
