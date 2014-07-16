# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0015_auto_20140716_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2014, 7, 16, 6, 30, 46, 286461), verbose_name='Publication Date', null=True),
        ),
    ]
