# Generated by Django 4.1 on 2023-02-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShadzBlogs', '0002_blogpost_content_head0_blogpost_content_head1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='ShadzBlogs/images'),
        ),
    ]
