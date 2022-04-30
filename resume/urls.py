from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('resume/', views.UploadView.as_view(), name='fileupload'),
    # path('resume_text/', views.resume_text, name='resume_text'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)