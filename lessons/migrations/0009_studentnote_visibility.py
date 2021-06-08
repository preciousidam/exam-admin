# Generated by Django 3.1.3 on 2021-05-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0008_auto_20210508_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentnote',
            name='visibility',
            field=models.CharField(choices=[(0, 'Private'), (1, 'Share with Friends')], default=0, max_length=50, verbose_name='Visibility'),
        ),
    ]
