# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0022_auto_20140716_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='Publication Date', default=datetime.datetime(2014, 7, 17, 5, 35, 34, 424017), blank=True),
        ),
    ]
