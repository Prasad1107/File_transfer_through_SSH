# Generated by Django 3.1.6 on 2021-02-18 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_filedownload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedownload',
            name='filepath_with_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='uploaddata',
            name='filepath',
            field=models.CharField(auto_created='Hey', max_length=100, verbose_name='file_path/file_name'),
        ),
    ]
