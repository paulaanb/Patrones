from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ("peticion", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lineapeticion", old_name="peticio_id", new_name="peticion",
        ),
    ]
