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
def index(request):
    jobs = Job.objects.all()
    job_name_list = [job.name for job in jobs]  # 직업의 이름만 추출
    context = {
        'job_list': job_name_list
    }
    return render(request, 'index.html', context)

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
    print(skill)
    top_repositories = (
        Repository.objects
        .filter(skill__name=skill)  # 해당 스킬에 속하는 저장소만 필터링
        .order_by('-repo_view')[:5]
        .values('repo_title', 'repo_url', 'repo_view', 'repo_img', 'repo_stars', 'repo_forks', 'repo_writer', 'repo_recent_time')
    )
    # 스킬에 해당하는 질문 중 조회수가 가장 높은 5개의 정보를 가져옵니다.
    top_questions = (
        Question.objects
        .filter(skill__name=skill)  # 해당 스킬에 속하는 질문만 필터링
        .order_by('-qs_view')[:5]
        .values('qs_title', 'qs_url', 'qs_view', 'qs_img', 'qs_votes', 'qs_answer', 'qs_writer')
    )
    print(top_questions)
    print(top_repositories)
    return Response({
        "top_repositories": list(top_repositories),
        "top_questions": list(top_questions),
    })

#------------------------------------------------------------
# 스킬 하나에 묶인 직군들
@api_view(['GET'])
def job_list_by_skill(request, skill):
    # 기술 이름에 해당하는 직군을 필터링하고, 중복을 제거하여 유니크한 값만 가져옴
    jobs = (
        Job.objects
        .filter(skill__name=skill)  # 기술의 이름을 필터링
        .values('name')  # 직군의 이름만 가져옴
        .distinct()  # 중복을 제거하여 유니크한 값만 가져옴
        .annotate(count=Count('name')) # 직군의 이름을 기준으로 그룹핑
        .order_by('name')  # 이름 순으로 정렬
    )
    job_count = {job['name']: job['count'] for job in jobs}
    return Response(job_count)