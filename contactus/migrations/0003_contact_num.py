# Generated by Django 3.1.2 on 2020-10-15 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0002_remove_contact_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='num',
            field=models.CharField(default='No phone number', max_length=10),
        ),
    ]