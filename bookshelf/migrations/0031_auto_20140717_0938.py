# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0030_auto_20140717_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(default='', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2014, 7, 17, 9, 38, 50, 251832), blank=True, null=True, verbose_name='Publication Date'),
        ),
    ]
