from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from app1 import views
from .views import FileView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    path(r'upload', views.upload),
    path(r'download', views.download),
    path(r'api', views.FileView.as_view(), name='api'),
    url(r'files', views.files_list),
]