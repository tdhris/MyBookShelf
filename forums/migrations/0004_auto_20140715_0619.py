# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, to_field='id', blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='creator',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, to_field='id', blank=True),
        ),
    ]
