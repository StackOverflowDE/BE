from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Job, Skill, Repository, Question
from .serializers import (
    JobSerializer,
    SkillSerializer,
    RepositorySerializer,
    QuestionSerializer,
)


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


@api_view(['GET'])
def top_repositories(request):
    # fork 수를 기준으로 상위 5개의 Repository 데이터를 가져옵니다.
    top_repositories = Repository.objects.order_by('-forks')[:10]
    
    # 템플릿 파일을 렌더링하고, 상위 레포지토리 데이터를 템플릿에 전달합니다.
    return render(request, 'top_repositories.html', {'top_repositories': top_repositories})