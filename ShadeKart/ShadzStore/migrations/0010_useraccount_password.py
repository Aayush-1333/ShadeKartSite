# Generated by Django 4.1 on 2023-02-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShadzStore', '0009_useraccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='password',
            field=models.CharField(default='12345678', max_length=10),
        ),
    ]
