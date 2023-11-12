from pathlib import Path
from .models import SportsHall
import csv
from django.contrib.gis.geos import Point

sports_halls_csv = Path(__file__).resolve().parent / 'data' / 'sports_halls.csv'


def run():
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
            )
            sports_hall.save()
