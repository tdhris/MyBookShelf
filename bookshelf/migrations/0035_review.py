# encoding: utf8
from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookshelf', '0034_auto_20140717_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('test', models.TextField(default='')),
                ('reviewer', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('date', models.DateField(default=datetime.datetime(2014, 7, 18, 5, 50, 7, 802902), blank=True, null=True)),
                ('score', models.IntegerField(default=3, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
