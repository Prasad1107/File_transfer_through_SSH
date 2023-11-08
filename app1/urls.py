from django.urls import re_path
from django.contrib import admin
from django.urls import path
from app1 import views
from .views import FileView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', views.home),
    path(r'upload', views.upload),
    path(r'download', views.download),
    path(r'api', views.FileView.as_view(), name='api'),
    re_path(r'files', views.files_list),
]