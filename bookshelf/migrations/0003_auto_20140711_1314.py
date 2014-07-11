# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_book_synopsis'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(to='bookshelf.Author', to_field='id', default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='pub_date',
            field=models.DateField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='synopsis',
            field=models.TextField(default=''),
        ),
    ]
