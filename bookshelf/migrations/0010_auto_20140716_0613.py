# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0009_auto_20140716_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Publication Date', default=datetime.datetime.now),
        ),
    ]
