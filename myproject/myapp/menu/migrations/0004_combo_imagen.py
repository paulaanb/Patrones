from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0003_combo_componente_delete_producto_combo_componentes"),
    ]

    operations = [
        migrations.AddField(
            model_name="combo",
            name="imagen",
            field=models.ImageField(blank=True, null=True, upload_to="menu"),
        ),
    ]
