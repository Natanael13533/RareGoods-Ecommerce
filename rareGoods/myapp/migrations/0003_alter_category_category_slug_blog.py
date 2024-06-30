# Generated by Django 5.0.4 on 2024-04-27 14:38

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_category_date_product_date"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="category_slug",
            field=models.SlugField(unique=True),
        ),
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=50)),
                ("sub_description", models.CharField(max_length=100)),
                ("slug", models.SlugField()),
                ("description", models.TextField()),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                ("image", models.ImageField(default="", upload_to="blog/images")),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "tbblog",
            },
        ),
    ]
