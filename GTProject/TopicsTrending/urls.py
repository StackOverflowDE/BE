from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TopicsTrending.views import (
    JobViewSet,
    SkillViewSet,
    RepositoryViewSet,
    QuestionViewSet,
    top_repositories,
    
)

router = DefaultRouter()
router.register(r"jobs", JobViewSet)
router.register(r"skills", SkillViewSet)
router.register(r"repositories", RepositoryViewSet)
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path("api/jobs/", JobViewSet.as_view({"get": "list"}), name="job-list"),
    path("", include(router.urls)),
    path('top_repositories/', top_repositories, name='top_repositories'),
    
]
