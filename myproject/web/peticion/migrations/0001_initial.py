from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("menu", "0005_combo_precio"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Peticion",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "peticion",
                "verbose_name_plural": "peticiones",
                "db_table": "peticion",
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="LineaPeticion",
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
                ("cantidad", models.IntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "combo_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="menu.combo"
                    ),
                ),
                (
                    "peticio_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="peticion.peticion",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Línea Pedido",
                "verbose_name_plural": "Línea Pedidos",
                "db_table": "lineapedidos",
                "ordering": ["id"],
            },
        ),
    ]
