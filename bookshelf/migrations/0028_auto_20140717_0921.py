# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0027_auto_20140717_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='Publication Date', default=datetime.datetime(2014, 7, 17, 9, 21, 27, 169959), blank=True, null=True),
        ),
    ]
