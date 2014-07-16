# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0006_auto_20140716_0605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 7, 16, 6, 5, 56, 105154), verbose_name='Publication Date'),
        ),
    ]
