# Generated by Django 2.2.7 on 2019-12-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20191201_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='cv',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]