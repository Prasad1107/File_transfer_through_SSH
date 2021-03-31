# Generated by Django 3.1.6 on 2021-02-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210218_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='downloaddata',
            name='filename',
        ),
        migrations.AddField(
            model_name='downloaddata',
            name='ssh_pass',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='ssh_pass',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filedownload',
            name='ssh_pass',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploaddata',
            name='ssh_pass',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='downloaddata',
            name='filepath',
            field=models.CharField(max_length=100, verbose_name='file_path/file_name'),
        ),
        migrations.AlterField(
            model_name='uploaddata',
            name='filepath',
            field=models.CharField(max_length=100, verbose_name='file_path/file_name'),
        ),
    ]
