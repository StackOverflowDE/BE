from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TopicsTrending.views import (
    JobViewSet,
    SkillViewSet,
    RepositoryViewSet,
    QuestionViewSet,
    job_list,
    skill_list,
    repo_list
)

router = DefaultRouter()
router.register(r"jobs", JobViewSet)
router.register(r"skills", SkillViewSet)
router.register(r"repositories", RepositoryViewSet)
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('jobs/', job_list, name='job_list'),  # URL 패턴에 이름 추가
    path('skill/', skill_list, name='skill_list'),
    path('repo/', repo_list, name='repo_list'),
    path('index/', job_list, name='index'),  # URL 패턴에 이름 추가
]