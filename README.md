

실행 순서

1. main에서 rocal repo에 git clone
2. rocal repo에서 python -m venv venv
 ![image](https://github.com/StackOverflowDE/BE/assets/162904282/e66c8986-6bcd-420e-b45a-8a4ecf6fc32a)
3. rocal repo에서 .\venv\Scripts\activate
 ![image](https://github.com/StackOverflowDE/BE/assets/162904282/6f42cbea-d599-48c4-9dfb-0c139a19521a)
4. rocal repo에서 python manage.py makemigrations
5. rocal repo에서 python manage.py migrate
6. rocal repo에서 python -m pip install Django
7. rocal repo에서 python -m pip install djangorestframework
8. rocal repo에서 python manage.py runserver (실행)

DB 활용
1. rocal repo에서 python createsuperuser (DB 접속을 위한)


