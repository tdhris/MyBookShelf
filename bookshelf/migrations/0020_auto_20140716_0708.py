# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0019_auto_20140716_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='Publication Date', blank=True, default=datetime.datetime(2014, 7, 16, 7, 8, 51, 428593)),
        ),
    ]
