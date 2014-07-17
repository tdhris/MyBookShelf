# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0032_auto_20140717_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='Publication Date', default=datetime.datetime(2014, 7, 17, 12, 19, 39, 376278), null=True, blank=True),
        ),
    ]
