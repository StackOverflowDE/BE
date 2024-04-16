from django.db import models
from django.utils import timezone

class Skill(models.Model):
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    job = models.ForeignKey('Job', on_delete=models.CASCADE, null=True)


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
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)


    @classmethod
    def add_data_from_file(cls, file_path):
        # 텍스트 파일 열기
        with open(file_path, 'r', encoding='utf-8') as file:
            # 각 줄을 읽어와 데이터베이스에 추가
            for line in file:
                # 줄을 쉼표로 분할하여 필드 값 가져오기
                fields = line.strip().split(',')
                # 데이터베이스에 추가
                cls.objects.create(
                    title=fields[0],
                    url=fields[1],
                    created_at=timezone.datetime.fromisoformat(fields[2]),
                    updated_at=timezone.datetime.fromisoformat(fields[3]),
                    forks=int(fields[4]),
                    img=fields[5],
                    repo_created_at=timezone.datetime.fromisoformat(fields[6]),
                    repo_tags=fields[7],
                    stars=int(fields[8]),
                    view=int(fields[9])
                )


class Question(models.Model):
    title = models.CharField(max_length=100, default='', null=False)
    url = models.CharField(max_length=100, default='', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    view = models.IntegerField(default=0)
    question_tags = models.CharField(max_length=100, default='', null=False)
    img = models.CharField(max_length=100, default='')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)


class Job(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)