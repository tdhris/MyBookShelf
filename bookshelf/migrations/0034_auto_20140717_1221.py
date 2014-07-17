# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0033_auto_20140717_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='Publication Date', null=True, blank=True, default=datetime.datetime(2014, 7, 17, 12, 21, 15, 476369)),
        ),
    ]
