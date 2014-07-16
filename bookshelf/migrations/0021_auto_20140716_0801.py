# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0020_auto_20140716_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, default=datetime.datetime(2014, 7, 16, 8, 1, 13, 534802), blank=True, verbose_name='Publication Date'),
        ),
    ]
