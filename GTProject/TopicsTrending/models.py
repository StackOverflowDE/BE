from django.db import models
from django.utils import timezone


class Skill(models.Model):
    name = models.CharField(max_length=100, null=False)
    repository = models.ForeignKey("Repository", on_delete=models.CASCADE, null=False)
    question = models.ForeignKey("Question", on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Repository(models.Model):
    title = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Question(models.Model):
    title = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Job(models.Model):
    name = models.CharField(max_length=100, null=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
