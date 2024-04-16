from rest_framework import serializers
from .models import Job, Skill, Repository, Question, TechBlog


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class TechBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechBlog
        fields = "__all__"
