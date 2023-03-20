# Generated by Django 4.1.7 on 2023-03-19 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0002_categorias"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="categoria_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="videos.categorias",
            ),
        ),
    ]
