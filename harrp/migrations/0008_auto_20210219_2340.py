# Generated by Django 3.1.3 on 2021-02-19 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harrp', '0007_auto_20210219_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='schools',
        ),
        migrations.AddField(
            model_name='school',
            name='students',
            field=models.ManyToManyField(to='harrp.StudentProfile', verbose_name='Students'),
        ),
    ]
