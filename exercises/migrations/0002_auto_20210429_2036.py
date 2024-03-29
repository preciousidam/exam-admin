# Generated by Django 3.1.3 on 2021-04-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='exercise', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='answer',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Answer'),
        ),
    ]
