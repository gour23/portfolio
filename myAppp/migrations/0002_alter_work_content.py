# Generated by Django 4.1.2 on 2023-01-23 11:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myAppp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
