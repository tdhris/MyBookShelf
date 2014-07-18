# encoding: utf8
from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0038_auto_20140718_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(default=datetime.datetime(2014, 7, 18, 6, 14, 14, 90287), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='Publication Date', default=datetime.datetime(2014, 7, 18, 6, 14, 14, 89483), null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(null=True, blank=True, to_field='id', to=settings.AUTH_USER_MODEL),
        ),
    ]
