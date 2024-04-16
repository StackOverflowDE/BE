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
                    created_at=timezone.datetime.strptime(fields[2], '%Y-%m-%d %H:%M:%S'),
                    updated_at=timezone.datetime.strptime(fields[3], '%Y-%m-%d %H:%M:%S')
                )



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
