# Generated by Django 4.1 on 2022-11-03 17:40

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0015_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=django_quill.fields.QuillField(),
        ),
    ]
