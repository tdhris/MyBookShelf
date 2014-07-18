# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0037_auto_20140718_0551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='test',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 7, 18, 6, 7, 10, 391689), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2014, 7, 18, 6, 7, 10, 390886), verbose_name='Publication Date', null=True, blank=True),
        ),
    ]
