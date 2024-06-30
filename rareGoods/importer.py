import os
import sys
sys.path.append(os.path.abspath(os.path.join(__file__, *[os.pardir] * 3)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'rareGoods.settings'
import django
django.setup()

from myapp.models import Lokasi
import csv

import time
start_time = time.time()

with open('./csv_data/Lokasi.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for num, row in enumerate(reader):
        if not Lokasi.objects.filter(pk=num+1).exists():
            Lokasi.objects.create(toko=row["toko"], 
                                       kota=row["kota"],
                                       provinsi=row["provinsi"],
                                       alamat=row["alamat"],
                                       latitude=float(row["latitude"]),
                                       longitude=float(row["longitude"])),

print("--- %s seconds ---" % (time.time() - start_time))