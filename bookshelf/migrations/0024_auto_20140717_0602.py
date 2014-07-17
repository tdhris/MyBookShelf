# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0023_auto_20140717_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='Publication Date', null=True, default=datetime.datetime(2014, 7, 17, 6, 2, 5, 974218), blank=True),
        ),
    ]
