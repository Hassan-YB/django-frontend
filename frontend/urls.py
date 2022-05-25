from django.urls import path, include, re_path
from .views import *

app_name = 'frontend'

urlpatterns = [
    path('', Index.as_view(), name="Index"),
    path('signup/', SignUp.as_view(), name="SignUp"),
    path('signup-parent/', ParentSignUp.as_view(), name="ParentSignUp"),
    path('signup-teacher/', TeacherSignUp.as_view(), name="TeacherSignUp"),
    path('teacher-onboarding/', TeacherOnboarding.as_view(), name="TeacherOnboarding"),
]