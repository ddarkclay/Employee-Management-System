# Generated by Django 2.2.3 on 2019-08-08 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190804_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='picture/%Y/%m/%d/'),
        ),
    ]
