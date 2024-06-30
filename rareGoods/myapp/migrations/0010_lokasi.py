# Generated by Django 5.0.4 on 2024-06-30 06:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0009_alter_product_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lokasi",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("toko", models.CharField(max_length=200)),
                ("kota", models.CharField(max_length=200)),
                ("provinsi", models.CharField(max_length=150)),
                ("alamat", models.CharField(max_length=300)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
            options={
                "db_table": "tblokasi",
            },
        ),
    ]