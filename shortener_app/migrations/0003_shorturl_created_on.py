# Generated by Django 2.1.2 on 2018-11-24 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0002_shorturl_clicks'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime.utcnow),
        ),
    ]
