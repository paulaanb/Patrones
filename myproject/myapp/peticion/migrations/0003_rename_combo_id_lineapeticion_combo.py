from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("peticion", "0002_rename_peticio_id_lineapeticion_peticion"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lineapeticion", old_name="combo_id", new_name="combo",
        ),
    ]
