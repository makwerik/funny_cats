# Generated by Django 5.1.1 on 2024-09-14 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='is_furry',
            field=models.BooleanField(default=True),
        ),
    ]
