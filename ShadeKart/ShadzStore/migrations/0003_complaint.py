# Generated by Django 4.1 on 2023-02-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShadzStore', '0002_alter_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=60)),
                ('email', models.CharField(default='', max_length=30)),
                ('phone', models.IntegerField(default=0)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
