# Generated by Django 4.1 on 2022-11-03 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0012_alter_post_imagen_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]