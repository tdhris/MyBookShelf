# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0017_auto_20140716_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2014, 7, 16, 6, 44, 23, 488238), blank=True, null=True, verbose_name='Publication Date'),
        ),
    ]
