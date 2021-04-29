# Generated by Django 3.1.3 on 2021-04-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harrp', '0010_auto_20210220_0057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentprofile',
            options={'ordering': ['user__first_name', 'user__last_name', 'level']},
        ),
        migrations.AlterField(
            model_name='school',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, related_name='schools', to='harrp.StudentProfile', verbose_name='students'),
        ),
    ]