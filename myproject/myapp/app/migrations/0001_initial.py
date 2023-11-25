from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pizza",
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
                ("masa", models.CharField(max_length=255)),
                ("salsa", models.CharField(max_length=255)),
                ("ingredientes_principales", models.CharField(max_length=255)),
                ("coccion", models.CharField(max_length=255)),
                ("presentacion", models.CharField(max_length=255)),
                ("maridaje_recomendado", models.CharField(max_length=255)),
                ("extra", models.CharField(max_length=255)),
            ],
        ),
    ]
