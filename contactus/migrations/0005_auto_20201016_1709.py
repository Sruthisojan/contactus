# Generated by Django 3.1.2 on 2020-10-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0004_auto_20201016_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='num',
            field=models.CharField(max_length=10),
        ),
    ]
