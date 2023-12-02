from pathlib import Path
from .models import SportsHall
import csv
from django.contrib.gis.geos import Point
from django.contrib.auth import authenticate

sports_halls_csv = Path(__file__).resolve().parent / 'data' / 'sports_halls.csv'


def run():
    username = input('Enter your username:')
    password = input('Enter your password:')

    user = authenticate(username=username, password=password)

    if user is not None:
        with open(sports_halls_csv) as file:
            reader = csv.reader(file)
            # pass the header
            next(reader)

            SportsHall.objects.all().delete()

            for row in reader:
                print(row)
                lon = float(row[2])
                lat = float(row[3])

                sports_hall = SportsHall(
                    hall_name=row[0],
                    address=row[1],
                    location=Point(lon, lat),
                    courts=int(row[4]),
                    phone_no=row[5],
                    created_by=user.profile,
                )
                sports_hall.save()
    else:
        print("Username/Password incorrect, please try again.")
