# Generated by Django 2.2.3 on 2019-08-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_auto_20190808_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(to='poll.Tag'),
        ),
    ]