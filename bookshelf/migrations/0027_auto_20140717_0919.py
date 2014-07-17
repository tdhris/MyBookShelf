# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0026_auto_20140717_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='biography',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, default=datetime.datetime(2014, 7, 17, 9, 19, 54, 979861), blank=True, verbose_name='Publication Date'),
        ),
    ]
