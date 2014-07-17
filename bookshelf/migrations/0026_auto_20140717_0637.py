# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0025_auto_20140717_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='Publication Date', blank=True, null=True, default=datetime.datetime(2014, 7, 17, 6, 37, 14, 608668)),
        ),
    ]
