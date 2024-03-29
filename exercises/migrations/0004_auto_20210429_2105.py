# Generated by Django 3.1.3 on 2021-04-29 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_auto_20210428_2029'),
        ('exercises', '0003_auto_20210429_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='lesson',
        ),
        migrations.AddField(
            model_name='exercise',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exercises', to='lessons.lesson', verbose_name='Topic'),
        ),
    ]
