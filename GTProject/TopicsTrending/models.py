from django.db import models
from django.utils import timezone

class Job(models.Model):
    name = models.CharField(max_length=100, default='', null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Skill(models.Model):
    name = models.CharField(max_length=100, null=False)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        if self.pk:  # Check if the Skill object already exists
            # If it exists, update the count directly
            existing_skill = Skill.objects.filter(name=self.name, job=self.job).first()
            if existing_skill:
                existing_skill.count += 1
                existing_skill.save(update_fields=['count'])
        else:
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
    repo_tags = models.CharField(max_length=100, default='')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)


    @classmethod
    def add_data_from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                fields = line.strip().split(',')
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
