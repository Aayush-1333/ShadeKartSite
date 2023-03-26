# Generated by Django 4.1 on 2023-02-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShadzStore', '0003_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(default='', max_length=90)),
                ('address1', models.CharField(default='', max_length=80)),
                ('address2', models.CharField(default='', max_length=80)),
                ('address3', models.CharField(default='', max_length=80)),
                ('state', models.CharField(default='', max_length=40)),
                ('city', models.CharField(default='', max_length=20)),
                ('zipcode', models.CharField(default='', max_length=7)),
                ('contact_number', models.CharField(default='', max_length=13)),
                ('email_address', models.CharField(default='', max_length=90)),
            ],
        ),
    ]