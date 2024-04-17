from django.db import models
from django.utils import timezone

class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    job = models.ForeignKey('Job', on_delete=models.CASCADE, null=True)

    @classmethod
    def add_data_from_file(cls, file_path):
        # 텍스트 파일 열기
        with open(file_path, 'r', encoding='utf-8') as file:
            # 각 줄을 읽어와 데이터베이스에 추가
            for line in file:
                # 줄을 쉼표로 분할하여 필드 값 가져오기
                fields = line.strip().split(',')
                try:
                    job_instance = Job.objects.get(id=int(fields[4]))  # 외래 키로 사용될 Job 모델의 인스턴스 가져오기
                    # 데이터베이스에 추가
                    cls.objects.create(
                        id = fields[0],
                        name=fields[1],
                        created_at=timezone.datetime.fromisoformat(fields[2]),
                        updated_at=timezone.datetime.fromisoformat(fields[3]),
                        job=job_instance
                    )
                except ValueError as e:
                    print(f"Error adding data: {e}")
                except Job.DoesNotExist as e:
                    print(f"Error adding data: {e}")


class Repository(models.Model):
    id = models.AutoField(primary_key=True)
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
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, null=True)


    @classmethod
    def add_data_from_file(cls, file_path):
        # 텍스트 파일 열기
        with open(file_path, 'r', encoding='utf-8') as file:
            # 각 줄을 읽어와 데이터베이스에 추가
            for line in file:
                # 줄을 쉼표로 분할하여 필드 값 가져오기
                fields = line.strip().split(',')
                try:
                    # 데이터베이스에 추가
                    skill_instance = Skill.objects.get(id=int(fields[11]))  # 외래 키로 사용될 Skill 모델의 인스턴스 가져오기
                    cls.objects.create(
                        id=fields[0],
                        title=fields[1],
                        url=fields[2],
                        created_at=timezone.datetime.fromisoformat(fields[3]),
                        updated_at=timezone.datetime.fromisoformat(fields[4]),
                        forks=int(fields[5]),
                        img=fields[6],
                        repo_created_at=timezone.datetime.fromisoformat(fields[7]),
                        repo_tags=fields[8],
                        stars=int(fields[9]),
                        view=int(fields[10]),
                        skill=skill_instance
                    )
                except ValueError as e:
                    print(f"Error adding data: {e}")
                except Job.DoesNotExist as e:
                    print(f"Error adding data: {e}")

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='', null=False)
    url = models.CharField(max_length=100, default='', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    view = models.IntegerField(default=0)
    question_tags = models.CharField(max_length=100, default='', null=False)
    img = models.CharField(max_length=100, default='')
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE, null=True)


    @classmethod
    def add_data_from_file(cls, file_path):
        # 텍스트 파일 열기
        with open(file_path, 'r', encoding='utf-8') as file:
            # 각 줄을 읽어와 데이터베이스에 추가
            for line in file:
                # 줄을 쉼표로 분할하여 필드 값 가져오기
                fields = line.strip().split(',')
                # 데이터베이스에 추가
                try:
                    skill_instance = Skill.objects.get(id=int(fields[8]))  # 외래 키로 사용될 Skill 모델의 인스턴스 가져오기
                    # 데이터베이스에 추가
                    cls.objects.create(
                        id=fields[0],
                        title=fields[1],
                        url=fields[2],
                        created_at=timezone.datetime.fromisoformat(fields[3]),
                        updated_at=timezone.datetime.fromisoformat(fields[4]),
                        view=int(fields[5]),
                        question_tags=fields[6],
                        img=fields[7],
                        skill=skill_instance
                    )
                except ValueError as e:
                    print(f"Error adding data: {e}")
                except Job.DoesNotExist as e:
                    print(f"Error adding data: {e}")



class Job(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)