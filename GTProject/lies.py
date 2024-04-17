from faker import Faker
import random

import os

current_directory = os.path.dirname(os.path.abspath(__name__))
skill_file_path = os.path.join(current_directory, 'test_skill_data.txt')
question_file_path = os.path.join(current_directory, 'test_question_data.txt')
repo_file_path = os.path.join(current_directory, 'test_repo_data.txt')

fake = Faker()

def random_skill(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for i in range(1, 51):  # 50개의 가짜 데이터 생성
            data_line = f"{i},{fake.name()},{fake.iso8601()},{fake.iso8601()},{random.randint(2, 6)}\n"
            file.write(data_line)


def random_question(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for i in range(1, 1001):  # 10개의 가짜 데이터 생성
            data_line = (f"{i}, {fake.sentence()}"
                         f",{fake.url()}"
                         f",{fake.iso8601()}"
                         f",{fake.iso8601()}"
                         f",{random.randint(0, 10000)}"
                         f",{' '.join(fake.words())}"
                         f",{fake.image_url()}"
                         f",{random.randint(1, 50)}\n")
            file.write(data_line)


def random_repo(file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for i in range(1, 1001):  # 10개의 가짜 데이터 생성
            data_line = f"{i}, {fake.sentence()},{fake.url()},{fake.iso8601()},{fake.iso8601()},{random.randint(0, 1000)},{fake.image_url()},{fake.iso8601()},{' '.join(fake.words())},{random.randint(0, 1000)},{random.randint(0, 10000)}, {random.randint(1, 50)}\n"
            file.write(data_line)

random_skill(skill_file_path)
random_question(question_file_path)
random_repo(repo_file_path)



