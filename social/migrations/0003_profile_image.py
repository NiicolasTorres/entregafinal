# Generated by Django 4.1 on 2022-10-31 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_rename_context_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='batman.png', upload_to=''),
        ),
    ]
