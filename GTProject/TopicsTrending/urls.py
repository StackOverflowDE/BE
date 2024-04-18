from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TopicsTrending.views import (
    JobViewSet,
    SkillViewSet,
    RepositoryViewSet,
    QuestionViewSet,
    # job_list,
    index,
    skill_list,
    info_list,
    job_list_by_skill
)

router = DefaultRouter()
router.register(r"jobs", JobViewSet)
router.register(r"skills", SkillViewSet)
router.register(r"repositories", RepositoryViewSet)
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('skill-list/<str:job>/', skill_list, name='skill_list'),
    path('info-list/<str:skill>/', info_list, name='info_list'),
    path('job-list-by-skill/<str:skill>', job_list_by_skill, name='job_list_by_skill'),
]