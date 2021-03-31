from django.db import models
from django.conf import settings

class UploadData(models.Model):
    filepath = models.CharField(max_length=100,verbose_name="file_path/file_name")
    hostname = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=30)
    destination_location= models.CharField(max_length=100)
    ssh_pass = models.CharField(max_length=30)

    class Meta:  
        db_table = "UploadData"

class DownloadData(models.Model):
    filepath = models.CharField(max_length=100,verbose_name="file_path/file_name")
    hostname = models.CharField(max_length=30)
    ip_address = models.CharField(max_length=30)
    local_path = models.CharField(max_length=100)
    ssh_pass = models.CharField(max_length=30)

    class Meta:  
        db_table = "DownloadData"


class FileUpload(models.Model):
    fname = models.FileField(blank=False, null=False)
    hostname = models.CharField(max_length=20)
    dest_ip = models.CharField(max_length=20)
    dest_file_location = models.CharField(max_length=20)
    ssh_pass = models.CharField(max_length=30)


class FileDownload(models.Model):
    hostname = models.CharField(max_length=20)
    dest_ip = models.CharField(max_length=20)
    filepath_with_name = models.CharField(max_length=50)
    ssh_pass = models.CharField(max_length=30)


