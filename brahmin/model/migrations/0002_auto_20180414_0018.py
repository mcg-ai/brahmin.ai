# Generated by Django 2.0.4 on 2018-04-13 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inst',
            name='confidance',
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inst',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 14, 0, 17, 42, 408713)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inst',
            name='docs',
            field=models.TextField(default='Hello. This is some documentation'),
            preserve_default=False,
        ),
    ]
