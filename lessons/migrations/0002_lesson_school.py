# Generated by Django 3.1.3 on 2021-02-20 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('harrp', '0010_auto_20210220_0057'),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='harrp.school', verbose_name=''),
        ),
    ]
