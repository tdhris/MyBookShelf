# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0036_auto_20140718_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 7, 18, 5, 51, 37, 584840), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2014, 7, 18, 5, 51, 37, 584018), null=True, blank=True, verbose_name='Publication Date'),
        ),
    ]
