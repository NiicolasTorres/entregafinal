# Generated by Django 4.1 on 2022-11-02 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(null=True, upload_to='posteos'),
        ),
    ]
