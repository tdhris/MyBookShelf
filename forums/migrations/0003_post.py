# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forums', '0002_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('topic', models.ForeignKey(to='forums.Topic', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
