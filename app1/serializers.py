from rest_framework import serializers
from .models import FileUpload,FileDownload


class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = FileUpload
    fields = ('fname', 'hostname','dest_ip','dest_file_location','ssh_pass')

class FileDownloader(serializers.ModelSerializer):
  class Meta():
    model = FileDownload
    fields = ('hostname','dest_ip','filepath_with_name','ssh_pass')
    