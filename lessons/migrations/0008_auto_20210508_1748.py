# Generated by Django 3.1.3 on 2021-05-08 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0007_auto_20210508_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentnote',
            name='shared',
            field=models.ManyToManyField(related_name='Note', to=settings.AUTH_USER_MODEL, verbose_name='Shared With'),
        ),
        migrations.AlterField(
            model_name='studentnote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
    ]