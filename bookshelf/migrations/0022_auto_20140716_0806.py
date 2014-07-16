# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0021_auto_20140716_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, blank=True, default=datetime.datetime(2014, 7, 16, 8, 6, 43, 499540), verbose_name='Publication Date'),
        ),
    ]
