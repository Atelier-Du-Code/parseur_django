
from django.urls import path

from app_upload.views import index, upload_document



urlpatterns = [
    path('', index, name="index-upload"),
    path('docs/', upload_document, name='upload_document'),
]
