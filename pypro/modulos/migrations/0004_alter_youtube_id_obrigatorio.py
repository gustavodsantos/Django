# Generated by Django 5.0.6 on 2024-07-04 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_aula_youtube_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='youtube_id',
            field=models.CharField(max_length=32),
        ),
    ]
