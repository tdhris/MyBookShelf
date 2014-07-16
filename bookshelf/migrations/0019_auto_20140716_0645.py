# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0018_auto_20140716_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, default=datetime.datetime(2014, 7, 16, 6, 45, 51, 121032), verbose_name='Publication Date', blank=True),
        ),
    ]
