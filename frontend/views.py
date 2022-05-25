from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

class Index(TemplateView):
    template_name = 'home.html'

class SignUp(TemplateView):
    template_name = 'signup.html'

class ParentSignUp(TemplateView):
    template_name = 'parent.html'

class TeacherSignUp(TemplateView):
    template_name = 'teacher.html'

class TeacherOnboarding(TemplateView):
    template_name = 'teacheronboarding.html'