from django.db import models
from django.utils import timezone
from django.db.models import Max

class Job(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name_job_id = models.CharField(max_length=200, default='', null=False)

    def save(self, *args, **kwargs):
        if not self.id:
            # 새로운 객체인 경우에만 처리
            max_id = Skill.objects.all().aggregate(models.Max('id'))['id__max'] or 0
            self.id = max_id + 1
        # name_job_id 생성 (name과 job 조합)
        self.name_job_id = f"{self.name}_{self.job_id}"
        super().save(*args, **kwargs)

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
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)



class Question(models.Model):
    title = models.CharField(max_length=100, default='', null=False)
    url = models.CharField(max_length=100, default='', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    view = models.IntegerField(default=0)
    img = models.CharField(max_length=100, default='')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)
