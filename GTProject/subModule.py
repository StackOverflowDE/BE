import os
from TopicsTrending.models import Repository

current_directory = os.path.dirname(os.path.abspath(__name__))
file_path = os.path.join(current_directory, 'test_data.txt')
Repository.add_data_from_file(file_path)

# python manage.py shell 에서 사용된다.
# exec(open("./subModule.py").read())

