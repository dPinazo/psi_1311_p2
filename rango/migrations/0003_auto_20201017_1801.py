# Generated by Django 2.1.5 on 2020-10-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20201017_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(default=0),
        ),
    ]
