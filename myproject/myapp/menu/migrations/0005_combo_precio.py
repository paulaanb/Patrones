from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu", "0004_combo_imagen"),
    ]

    operations = [
        migrations.AddField(
            model_name="combo",
            name="precio",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
