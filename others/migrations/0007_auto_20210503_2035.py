# Generated by Django 3.1.3 on 2021-05-03 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0006_auto_20210503_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='level',
            field=models.ManyToManyField(related_name='subjects', to='others.Level', verbose_name='Level'),
        ),
    ]