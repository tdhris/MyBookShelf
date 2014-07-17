# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0029_auto_20140717_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.TextField(null=True, default='', blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='genre',
            name='biography',
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='Publication Date', default=datetime.datetime(2014, 7, 17, 9, 23, 50, 202154), blank=True),
        ),
    ]
