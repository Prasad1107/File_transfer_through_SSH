# Generated by Django 3.1.6 on 2021-02-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DownloadData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('filepath', models.CharField(max_length=100)),
                ('hostname', models.CharField(max_length=30)),
                ('ip_address', models.CharField(max_length=30)),
                ('local_path', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'DownloadData',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('remark', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UploadData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.CharField(max_length=100)),
                ('hostname', models.CharField(max_length=30)),
                ('ip_address', models.CharField(max_length=30)),
                ('destination_location', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'UploadData',
            },
        ),
    ]
