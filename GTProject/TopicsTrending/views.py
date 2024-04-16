from django.shortcuts import render
from rest_framework import viewsets
from .models import Job, Skill, Repository, Question, TechBlog
from .serializers import JobSerializer, SkillSerializer, RepositorySerializer, QuestionSerializer, TechBlogSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class TechBlogViewSet(viewsets.ModelViewSet):
    queryset = TechBlog.objects.all()
    serializer_class = TechBlogSerializer