from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import UploadForm, DownloadForm

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer,FileDownloader

from . import file_operation
from django.conf import settings
import os

import subprocess
# Create your views here.
  
def home(request):
      return render(request, 'home.html')

def upload(request):
    data = UploadForm()
   
    if request.method == "POST":
        #Get the posted form
        MyLoginForm = UploadForm(request.POST)
       
        if MyLoginForm.is_valid():
            fpath = MyLoginForm.cleaned_data['filepath']
            hname = MyLoginForm.cleaned_data['hostname']
            ip = MyLoginForm.cleaned_data['ip_address']
            dest = MyLoginForm.cleaned_data['destination_location']
            ssh_password = MyLoginForm.cleaned_data['ssh_pass']

            host_ip = f"{hname}@{ip}"

            output = file_operation.upload_data(fpath,host_ip,dest,ssh_password)
            print(output)
            if output.returncode == 0:
                return render(request, 'upload_again.html', {'output': "File Transfered succesfully"} )
            elif output.returncode == 1 or output.returncode == 5:
                return render(request, 'upload_again.html',{'output': output.stderr})
            else:
                return render(request, 'upload.html', {'form': UploadForm})

    else:
        MyLoginForm = UploadForm()
        return render(request, 'upload.html', {'form': UploadForm})
    
    
def download(request):
    data = DownloadForm()
   
    if request.method == "POST":
        #Get the posted form
        MyLoginForm = DownloadForm(request.POST)
       
        if MyLoginForm.is_valid():
            file_path = MyLoginForm.cleaned_data['filepath']
            hname = MyLoginForm.cleaned_data['hostname']
            ip = MyLoginForm.cleaned_data['ip_address']
            dest = MyLoginForm.cleaned_data['local_path']
            ssh_password = MyLoginForm.cleaned_data['ssh_pass']

            
            host_ip = f'{hname}@{ip}'

            output = file_operation.download_data(host_ip,file_path,dest,ssh_password)
            if output.returncode == 0:
                return render(request, 'download_again.html', {'output': "File Received succesfully"} )
            elif output.returncode == 1 or output.returncode == 5:
                return render(request, 'download_again.html',{'output': output.stderr})
            else:
                return render(request, 'download.html', {'form': DownloadForm})


    else:
        MyLoginForm = DownloadForm()
        return render(request, 'download.html', {'form': DownloadForm})


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
    
    
        if file_serializer.is_valid():
            file_serializer.save()
            fname = file_serializer.data['fname']
            fpath = str(settings.MEDIA_ROOT)+ '/'+fname.split('/media/')[1]
            hname = file_serializer.data['hostname']
            ip = file_serializer.data['dest_ip']
            host_ip = f'{hname}@{ip}'
            dest = file_serializer.data['dest_file_location']
            ssh_password = file_serializer.data['ssh_pass']


            print(fpath,host_ip,dest)
            output = file_operation.upload_data(fpath,host_ip,dest,ssh_password)
            if output.returncode == 0:
                return Response(data="File Sent successfully" )
            elif output.returncode == 1 or output.returncode == 5:
                return Response(data= output.stderr)
            else:
                return Response(file_serializer.data)
    
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        file_serializer = FileDownloader(data=request.data)
    
        if file_serializer.is_valid():
            file_serializer.save()
            print(file_serializer.data)
            hname = file_serializer.data['hostname']
            ip = file_serializer.data['dest_ip']
            host_ip = f'{hname}@{ip}'
            dest_path = file_serializer.data['filepath_with_name']
            local_path = str(settings.MEDIA_ROOT)
            ssh_password = file_serializer.data['ssh_pass']

            output = file_operation.download_data(host_ip,dest_path,local_path,ssh_password)
            if output.returncode == 0:
                return Response(data="File Received succesfully" )
            elif output.returncode == 1 or output.returncode == 5:
                return Response(data= output.stderr)
            else:
                return Response(file_serializer.data)
    
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def files_list(request):
    return render(request, 'files_list.html',{'total_files':os.listdir(settings.MEDIA_ROOT)})
