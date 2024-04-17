from django.shortcuts import render
from django.db.models import Count
from rest_framework import status
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

#------------------------------------------------------------
# 직업 목록을 가져오는 함수를 구현합니다.
@api_view(['GET'])
def job_list(request):
    jobs = Job.objects.all()
    job_name_list = [job.name for job in jobs]  # 직업의 이름만 추출
    return Response(job_name_list)

#------------------------------------------------------------
# 선택한 직업에 해당하는 기술들의 출현 횟수를 가져오는 함수를 구현합니다.
@api_view(['GET'])
def skill_list(request, job):

    job_skills = (
        Skill.objects
        .filter(job__name=job)
        .values('name')
        .annotate(count=Count('name'))
        .order_by('-count')[:5]  # 가장 많이 등장하는 5개의 기술만 가져옵니다.
    )
    job_count_skill = {skill['name']: skill['count'] for skill in job_skills}
    return Response(job_count_skill)

#------------------------------------------------------------
# 저장소와 질문 중 조회수가 가장 높은 5개의 정보를 가져오는 함수를 구현합니다.
@api_view(['GET'])
def info_list(request, skill):
    # 스킬에 해당하는 저장소 중 조회수가 가장 높은 5개의 정보를 가져옵니다.
    top_repositories = (
        Repository.objects
        .filter(skill__name=skill)  # 해당 스킬에 속하는 저장소만 필터링
        .order_by('-view')[:5]
        .values('title', 'url', 'view', 'img', 'stars', 'forks', 'repo_created_at')
    )
    # 스킬에 해당하는 질문 중 조회수가 가장 높은 5개의 정보를 가져옵니다.
    top_questions = (
        Question.objects
        .filter(skill__name=skill)  # 해당 스킬에 속하는 질문만 필터링
        .order_by('-view')[:5]
        .values('title', 'url', 'view', 'img')
    )
    return Response({
        "top_repositories": list(top_repositories),
        "top_questions": list(top_questions),
    })