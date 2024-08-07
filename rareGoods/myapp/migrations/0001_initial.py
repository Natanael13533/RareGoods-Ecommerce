# Generated by Django 5.0.4 on 2024-04-22 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("category_name", models.CharField(max_length=50)),
                ("category_slug", models.SlugField()),
            ],
            options={
                "db_table": "tbcategory",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                ("product_name", models.CharField(max_length=50)),
                ("slug", models.SlugField()),
                ("description", models.TextField()),
                ("price", models.IntegerField(default=0)),
                ("image", models.ImageField(default="", upload_to="product/images")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.category"
                    ),
                ),
            ],
            options={
                "db_table": "tbproduct",
            },
        ),
    ]
