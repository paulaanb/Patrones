from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0002_producto_created_producto_updated"),
    ]

    operations = [
        migrations.CreateModel(
            name="Combo",
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
                ("nombre", models.CharField(max_length=50)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
            ],
            options={"verbose_name": "combo", "verbose_name_plural": "combos",},
        ),
        migrations.CreateModel(
            name="Componente",
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
                ("nombre", models.CharField(max_length=50)),
                ("precio", models.FloatField()),
                ("imagen", models.ImageField(blank=True, null=True, upload_to="menu")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="menu.categoriaprod",
                    ),
                ),
            ],
            options={
                "verbose_name": "componente",
                "verbose_name_plural": "componentes",
            },
        ),
        migrations.DeleteModel(name="Producto",),
        migrations.AddField(
            model_name="combo",
            name="componentes",
            field=models.ManyToManyField(to="menu.componente"),
        ),
    ]
