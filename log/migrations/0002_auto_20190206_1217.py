# Generated by Django 2.1.5 on 2019-02-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='logimg/%Y/%m/%D', width_field='width_field'),
        ),
    ]