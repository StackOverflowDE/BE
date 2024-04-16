from django.db import models
from django.utils import timezone

class Skill(models.Model):
    name = models.CharField(max_length=100, null=False)
    repository = models.ForeignKey("Repository", on_delete=models.CASCADE)
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Repository(models.Model):
    title = models.CharField(max_length=100, default='', null=False)
    url = models.CharField(max_length=100, default='', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    forks = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)
    img = models.CharField(max_length=100, default='')
    view = models.IntegerField(default=0)
    repo_created_at = models.DateTimeField(default=timezone.now)
    repo_tags = models.CharField(max_length=100, default='')


    @classmethod
    def add_data_from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                fields = line.strip().split(',')
                cls.objects.create(
                    title=fields[0],
                    url=fields[1],
                    created_at=timezone.datetime.strptime(fields[2], '%Y-%m-%d %H:%M:%S'),
                    updated_at=timezone.datetime.strptime(fields[3], '%Y-%m-%d %H:%M:%S'),
                    forks=int(fields[4]),
                    stars=int(fields[5]),
                    img=fields[6],
                    view=int(fields[7]),
                    repo_created_at=timezone.datetime.strptime(fields[8], '%Y-%m-%d %H:%M:%S'),
                    repo_tags=fields[9]
                )


class Question(models.Model):
    title = models.CharField(max_length=100, default='', null=False)
    url = models.CharField(max_length=100, default='', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    view = models.IntegerField(default=0)
    question_tags = models.CharField(max_length=100, default='', null=False)
    img = models.CharField(max_length=100, default='')


class Job(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)