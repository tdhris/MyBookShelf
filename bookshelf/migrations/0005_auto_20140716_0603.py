# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0004_auto_20140714_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(null=True, blank=True, verbose_name='Publication Date'),
        ),
    ]
