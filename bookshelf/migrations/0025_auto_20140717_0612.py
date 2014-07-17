# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0024_auto_20140717_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(null=True, blank=True, default=datetime.datetime(2014, 7, 17, 6, 12, 28, 448636), verbose_name='Publication Date'),
        ),
    ]
