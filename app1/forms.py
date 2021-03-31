from django import forms  
from app1.models import UploadData,DownloadData

class UploadForm(forms.ModelForm):
    ssh_pass = forms.CharField(widget=forms.PasswordInput)
    class Meta:  
        model = UploadData  
        fields = "__all__"  

class DownloadForm(forms.ModelForm):
    ssh_pass = forms.CharField(widget=forms.PasswordInput)
    class Meta:  
        model = DownloadData  
        fields = "__all__"  