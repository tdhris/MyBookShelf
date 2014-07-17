# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0028_auto_20140717_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, blank=True, verbose_name='Publication Date', default=datetime.datetime(2014, 7, 17, 9, 22, 38, 799581)),
        ),
        migrations.AlterField(
            model_name='genre',
            name='biography',
            field=models.TextField(null=True, blank=True, default=''),
        ),
    ]
