# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0016_auto_20140716_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='Publication Date', default=datetime.datetime(2014, 7, 16, 6, 37, 35, 804336), blank=True),
        ),
    ]
