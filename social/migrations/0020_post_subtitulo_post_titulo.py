# Generated by Django 4.1 on 2022-11-05 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0019_alter_post_content_alter_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitulo',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='titulo',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]