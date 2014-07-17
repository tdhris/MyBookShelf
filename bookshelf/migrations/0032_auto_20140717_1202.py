# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0031_auto_20140717_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='Publication Date', blank=True, default=datetime.datetime(2014, 7, 17, 12, 2, 23, 461454), null=True),
        ),
    ]
