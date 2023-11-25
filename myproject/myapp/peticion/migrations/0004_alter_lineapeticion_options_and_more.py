from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("peticion", "0003_rename_combo_id_lineapeticion_combo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lineapeticion",
            options={
                "ordering": ["id"],
                "verbose_name": "Línea Peticion",
                "verbose_name_plural": "Líneas Peticiones",
            },
        ),
        migrations.AlterModelTable(name="lineapeticion", table="lineapeticiones",),
    ]
