from faker import Faker
import random

import os

current_directory = os.path.dirname(os.path.abspath(__name__))
file_path = os.path.join(current_directory, 'test_data.txt')

fake = Faker()

with open(file_path, 'w', encoding='utf-8') as file:
    for i in range(1, 1001):  # 10개의 가짜 데이터 생성
        data_line = f"{fake.sentence()},{fake.url()},{fake.iso8601()},{fake.iso8601()},{random.randint(0, 1000)},{fake.image_url()},{fake.iso8601()},{' '.join(fake.words())},{random.randint(0, 1000)},{random.randint(0, 10000)}, {random.randint(0, 10)}\n"
        file.write(data_line)