import os
from django.utils import timezone

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

current_directory = os.path.dirname(os.path.abspath(__name__))
file_path = os.path.join(current_directory, 'test_data.txt')
add_data_from_file(file_path)