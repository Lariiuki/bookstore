# Generated by Django 5.2 on 2025-05-13 22:12

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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("active", models.BooleanField(default=True)),
            ],
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
                ("title", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("price", models.PositiveIntegerField(null=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "categories",
                    models.ManyToManyField(
                        blank=True, related_name="product", to="product.category"
                    ),
                ),
            ],
        ),
    ]
