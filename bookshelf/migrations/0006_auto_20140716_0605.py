# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0005_auto_20140716_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Publication Date'),
        ),
    ]
