# Generated by Django 4.1 on 2023-02-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShadzStore', '0006_orderdetail_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='full_name',
            field=models.CharField(default='NA', max_length=90),
        ),
    ]