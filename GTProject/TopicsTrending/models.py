from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, null=False)
    repository = models.ForeignKey('Repository', on_delete=models.CASCADE, null=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, null=False)
    techBlog = models.ForeignKey('TechBlog', on_delete=models.CASCADE, null=False)

class Repository(models.Model):
    title = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=100, null=False)

class Question(models.Model):
    title = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=100, null=False)

class TechBlog(models.Model):
    title = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=100, null=False)

class Job(models.Model):
    name = models.CharField(max_length=100, null=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=False)
