# Generated by Django 4.1.2 on 2023-01-24 14:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myAppp', '0002_alter_work_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
    ]
