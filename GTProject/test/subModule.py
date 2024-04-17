import os
from TopicsTrending.models import *

current_directory = os.path.dirname(os.path.abspath(__name__))

file_skill_path = os.path.join(current_directory, 'test_skill_data.txt')
Skill.add_data_from_file(file_skill_path)

file_repo_path = os.path.join(current_directory, 'test_repo_data.txt')
Repository.add_data_from_file(file_repo_path)

file_question_path = os.path.join(current_directory, 'test_question_data.txt')
Question.add_data_from_file(file_question_path)


# python manage.py shell 에서 사용된다.
# exec(open("./subModule.py").read())

