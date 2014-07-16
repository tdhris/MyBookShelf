# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0014_auto_20140716_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='Publication Date', default=datetime.datetime(2014, 7, 16, 6, 22, 40, 135434)),
        ),
    ]
