from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="product",
        ),
        migrations.AddField(
            model_name="order",
            name="product",
            field=models.ManyToManyField(blank=True, related_name="orders", to="product.product"),
        ),
    ]
