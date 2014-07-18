# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0035_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('review_ptr', models.OneToOneField(to='bookshelf.Review', auto_created=True, primary_key=True, to_field='id', serialize=False)),
                ('book', models.ForeignKey(to='bookshelf.Book', to_field='id')),
            ],
            options={
            },
            bases=('bookshelf.review',),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2014, 7, 18, 5, 50, 7, 802099), verbose_name='Publication Date', blank=True, null=True),
        ),
    ]
