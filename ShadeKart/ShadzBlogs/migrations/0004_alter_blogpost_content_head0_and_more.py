# Generated by Django 4.1 on 2023-02-19 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShadzBlogs', '0003_alter_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content_head0',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content_head1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content_head2',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head0',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(upload_to='ShadzBlogs/images'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
    ]
