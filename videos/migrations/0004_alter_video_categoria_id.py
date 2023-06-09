# Generated by Django 4.1.7 on 2023-03-20 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("videos", "0003_video_categoria_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="categoria_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="videos.categorias",
            ),
        ),
    ]
