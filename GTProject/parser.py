import pdb
import csv
import os
# Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록한다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GTProject.settings")
import django
django.setup()
from TopicsTrending.models import *
from django.db.utils import IntegrityError
from datetime import datetime

current_dir = os.getcwd()
data_path = os.path.join(current_dir, 'assets', 'data')
img_path = os.path.join(current_dir, 'assets', 'img')


def job_data_parser():
    # CSV 파일 경로
    file_path = os.path.join(data_path, 'job_data.csv')

    # CSV 파일 열기
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        # CSV 파일을 읽어들이는데 사용할 reader 생성
        reader = csv.reader(csvfile)
        # reader 객체를 subscriptable하게 만들기 위해 각 행을 리스트로 저장
        rows = [row for row in reader]
        result, all_stack = job_skill_refactor(rows)

    return result, all_stack


def job_skill_refactor(rows):
    # 각 행을 순회하면서 데이터 읽기
    result = {}
    all_stack = set()

    for row in rows[1:]:
        categories = row[1].split(', ')
        skills = eval(row[2])

        for category in categories:
            if category not in result:
                result[category] = []
            for skill in skills:
                result[category].append(skill)

    for category in result:
        all_stack = all_stack | set(result[category])

    # len(result) 25 erp 빠짐
    # list(my_dict.keys())
    return result, all_stack


def job_skill_DB_loader(job_skill):
    for key in job_skill:
        print(job_skill[key])
        job = Job.objects.create(name=key)
        for skill in job_skill[key]:
            Skill.objects.create(name=skill, job=job, name_job_id=key)


def git_repo_parser():
    # CSV 파일 경로
    file_paths = os.path.join(data_path, 'git')
    for skill in os.listdir(file_paths):
        csv_path = os.path.join(file_paths, skill)
        # git CSV 파일 파싱
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            # CSV 파일을 읽어들이는데 사용할 reader 생성
            reader = csv.reader(csvfile)
            # reader 객체를 subscriptable하게 만들기 위해 각 행을 리스트로 저장
            rows = [row for row in reader]
            rows = rows[1:]

        # skill 값 추출
        skill = skill[9:]
        skill = skill[:-4]

        git_repo_DB_loader(skill, rows)


def git_repo_DB_loader(skill, repo_infos):
    for info in repo_infos:
        # print(info)
        tech_stack = Skill.objects.filter(name=skill).first()
        formatted_date_string = info[4].replace(',', '')
        formatted_date_string = formatted_date_string.replace('GMT+9', '+0900')
        date_time_obj = datetime.strptime(formatted_date_string, '%b %d %Y %I:%M %p %z')
        try:
            Repository.objects.create(skill=tech_stack,
                                      repo_title=info[0],
                                      repo_forks=int(info[1].replace(',', '')),
                                      repo_stars=int(info[2].replace(',', '')),
                                      repo_recent_time=date_time_obj,
                                      repo_writer=info[5],
                                      repo_url=info[6],
                                      repo_img=info[7] if len(info) == 8 else "")
        except IntegrityError:
            pass


def sof_question_parser():
    # CSV 파일 경로
    file_path = os.path.join(data_path, 'sof')
    for skill in os.listdir(file_path):
        # sof CSV 파일 파싱
        csv_path = os.path.join(file_path, skill)
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            # CSV 파일을 읽어들이는데 사용할 reader 생성
            reader = csv.reader(csvfile)
            # reader 객체를 subscriptable하게 만들기 위해 각 행을 리스트로 저장
            rows = [row for row in reader]
            rows = rows[1:]

        # skill 값 추출
        skill = skill[9:]
        skill = skill[:-4]

        sof_question_DB_loader(skill, rows)


def sof_question_DB_loader(skill, question_info):

    for info in question_info:
        print(info)
        tech_stack = Skill.objects.filter(name=skill).first()

        if info[5][-1] == 'k':  # 킬로 단위 처리
            view = str(int(info[5][:-1]) * 1000)
        elif info[5][-1] == 'm':  # 메가 단위 처리
            view = str(int(float(info[5][:-1]) * 1_000_000))
        else:
            view = info[5]

        try:
            Question.objects.create(skill=tech_stack,
                                      qs_title=info[0],
                                      qs_writer=info[2],
                                      qs_votes=info[3],
                                      qs_answer=info[4],
                                      qs_view=view,
                                      qs_url=info[6],
                                      qs_img=info[7] if len(info) == 8 else "")
        except IntegrityError:
            pass


if __name__ == '__main__':

    job_skill, all_skill = job_data_parser()
    job_skill_DB_loader(job_skill)

    git_repo_parser()
    sof_question_parser()





