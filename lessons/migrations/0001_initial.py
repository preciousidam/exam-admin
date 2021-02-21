# Generated by Django 3.1.3 on 2021-02-20 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('others', '0002_auto_20210220_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('feature_image', models.ImageField(blank=True, null=True, upload_to='featured', verbose_name='Featured Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='others.subject', verbose_name='Subject')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lessons', to='others.topic', verbose_name='Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255, verbose_name='Heading')),
                ('body', models.TextField(verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='lessons.lesson', verbose_name='Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='featured', verbose_name='Image')),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='lessons.paragraph', verbose_name='Paragraph')),
            ],
        ),
    ]