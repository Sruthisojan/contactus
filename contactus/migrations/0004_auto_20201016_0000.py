# Generated by Django 3.1.2 on 2020-10-15 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0003_contact_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='num',
            field=models.BigIntegerField(),
        ),
    ]
