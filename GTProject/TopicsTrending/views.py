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
def skill_list(request):
    selected_job = request.GET.get('job')
    
    if selected_job:
        # 선택한 직업에 해당하는 기술들을 가져옵니다.
        job_skills = (
            Skill.objects
            .filter(job__name=selected_job)
            .values('name')
            .annotate(count=Count('name'))
            .order_by('-count')[:5]  # 가장 많이 등장하는 5개의 기술만 가져옵니다.
        )
        job_count_skill = {skill['name']: skill['count'] for skill in job_skills}
        return Response(job_count_skill)
    else:
        return Response({"message": "Please select a job."}, status=status.HTTP_400_BAD_REQUEST)

#------------------------------------------------------------
# 포그 수가 가장 많은 rpository를 가져오는 함수를 구현합니다.
@api_view(['GET'])
def repo_list(request):
    # 요청에서 선택된 스킬의 ID를 가져옵니다.
    skill_id = request.GET.get('skill')

    if skill_id:
        # 선택된 스킬에 해당하는 레포지토리를 가져옵니다.
        repositories = Repository.objects.filter(skill_id=skill_id).order_by('-forks')[:5]
        
        # Serializer를 사용하여 데이터를 직렬화합니다.
        serializer = RepositorySerializer(repositories, many=True)
        
        return Response(serializer.data)
    else:
        return Response({"message": "Please select a skill."}, status=status.HTTP_400_BAD_REQUEST)

#------------------------------------------------------------
# 위에 제시된 두 가지 기능 중 하나만을 선택하여 반환하는 함수를 구현합니다.
@api_view(['GET'])
def info_list(request, type=None):
    if type == 'repo':
        repositories = Repository.objects.all().order_by('-stars')[:5]
        serializer = RepositorySerializer(repositories, many=True)
        return Response(serializer.data)
    elif type == 'question':
        questions = Question.objects.all().order_by('-views')[:5]
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
    else:
        return Response({"message": "Invalid type. Please select 'repo' or 'question'."}, status=status.HTTP_400_BAD_REQUEST)
