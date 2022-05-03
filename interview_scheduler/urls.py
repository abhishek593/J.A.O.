from django.urls import path
from account import views
from django.conf.urls.static import static
from . import views
from django.conf import settings
app_name = "interview_scheduler"

urlpatterns = [
    # path('employee/register/', views.employee_registration, name='employee-registration'),
    # path('employer/register/', views.employer_registration, name='employer-registration'),
    path('interviews/<int:id>/<int:job_id>/', views.applicant_interview_handler, name='applicant-interview-handler'),
    path('interviews/recruiter/<int:id>/<int:job_id>/', views.recruiter_interview_handler, name='recruiter-interview-handler'),
    # path('login/', views.user_logIn, name='login'),
    # path('logout/', views.user_logOut, name='logout'),
    # path('resume/', views.UploadView.as_view(), name='fileupload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
