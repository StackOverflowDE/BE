# StackHub

## 목차

- [프로젝트 주제](#프로젝트-주제)
- [프로젝트 소개](#프로젝트-소개)
- [기술 스택](#기술-스택)
- [협엽 명세](#협업-명세)
- [개발 인원](#개발-인원)
- [Easy-To-Use](#Easy-To-Use)

## 프로젝트 주제

프로그래머스 채용 공고 크롤링을 통한 기술스택과 기술스택의 레포지토리,질문 시각화

## 프로젝트 소개

<p align="justify">
기업에서 직무에 따라 원하는 기술스택이 다른데 우리가 하고자하는 직무의 기술스택이 어떤것이 있는지 알아보고 트렌드가 어떤지 확인하고 그 기술스택들이 github와 stackoverflow와 같은 개발자 커뮤니티에서는 우리와 같은 관심사를 가진 개발자들이 어떤 주제를 다루고 있고 또 어떤 문제들이 있는지 확인하며 한눈에 보기쉽게 그리고 이용하기 쉽게 하기 위해 선정하게 되었습니다.<br/>
<br/>

- [프로젝트 보고서](https://chivalrous-chili-f77.notion.site/3fe1616db3fa4cb08806753b37785a18)
- [결과물 소개 문서](https://www.canva.com/design/DAGC690HfWk/xYbHWDtp5okR22UI9sjZ_g/view?utm_content=DAGC690HfWk&utm_campaign=designshare&utm_medium=link&utm_source=editor)

</p>

<p align="center">
 
1. **표지**
    
 <img src="./image/project/firstpage.png" width="50%">

2. **시각화 페이지 직무별 스킬 인기도**

 <img src="./image/project/secondpage.png" width="50%">

3. **시각화 페이지 스킬별 github repositroy**

 <img src="./image/project/thirdpage-1.png" width="50%">

4. **시각화 페이지 스킬별 stackoverflow question**

 <img src="./image/project/thirdpage-2.png" width="50%">

</p>

<br>

## 기술 스택

python --version = python 3.12

### 1. BackEnd

<img src="./image/stack/backend/1.png" width="25%"> <img src="./image/stack/backend/2.png" width="30%">

### 2. FrontEnd

<img src="./image/stack/frontend/1.png" width="15%"> <img src="./image/stack/frontend/2.png" width="15%">

### 3. Crawling

<img src="./image/stack/crawling/3.png" width="20%"> <img src="./image/stack/crawling/2.png" width="30%"><br>
<img src="./image/stack/crawling/1.png" width="30%">

<br>

## 협업 명세

### 대시보드 디자인

<img width="671" alt="image" src="https://github.com/StackOverflowDE/StackHub_BE/assets/127376832/7a636ac6-091c-4cac-aa68-53821f129879" width="60%">

### ERD

<img src="https://github.com/StackOverflowDE/StackHub_BE/assets/127376832/db10c464-c78d-430a-9d46-10ae121e468e" alt="image" width="30%">

### API

<img src="https://github.com/StackOverflowDE/StackHub_BE/assets/127376832/04e09320-a834-44b6-80ec-03165963f9a2" alt="image" width="30%">
   
### 개발 인원

|                                                                 FrontEnd                                                                 |                                                                 BackEnd                                                                  |                                                                 BackEnd                                                                  |                                                                 Crawling                                                                 |                                                                 Crawling                                                                 |
| :--------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                  정승현                                                                  |                                                                  이승준                                                                  |                                                                  신용승                                                                  |                                                                  정기홍                                                                  |                                                                  이소윤                                                                  |
| <img src="https://github.com/StackOverflowDE/StackHub_BE/assets/127376832/d191badb-c7fc-47a1-820d-dc5fc2660e6b" alt="image" width="100"> | <img src="https://github.com/StackOverflowDE/StackHub_BE/assets/127376832/c5bc2462-888d-42fb-ba36-f90d05abc92f" alt="image" width="100"> | <img src="https://github.com/StackOverflowDE/StackHub_BE/assets/127376832/0c401c32-8934-4c07-a084-bcd99103c9d0" alt="image" width="100"> | <img src="https://github.com/StackOverflowDE/StackHub_BE/assets/127376832/e4135717-feb4-4e2c-b72b-c251a523538d" alt="image" width="100"> | <img src="https://github.com/StackOverflowDE/StackHub_BE/assets/127376832/809105d7-5817-4f71-8356-ef5d92fd5de3" alt="image" width="100"> |

- 데이터 크롤링
  - 이소윤 : 데이터 크롤링 및 전처리(프로그래머스)
  - 정기홍 : 데이터 크롤링 및 전처리(github, stackoverflow)
- 백엔드
  - 신용승 : DB 관리 및 크롤링 데이터 DB 적재 모듈 개발 + 결과물 소개 문서 작성
  - 이승준 : DB 관리 및 API 개발
- 프론트엔드
  - 정승현 : 웹 페이지 템플릿 작성 및 데이터 시각화

<br>

## Easy-To-Use

1. git clone

2. cd GTProject

3. python -m venv venv (가상환경 생성)

4. python -m pip install -r requirements.txt (라이브러리 생성)

5. python manage.py makemigrations

6. python manage.py migrate

7. 크롤링 파일 실행<br/>
   7-1. Programmers 로그인 후, python programmers_crawling.py<br/>
   7-2. Github 로그인 후, python crawling.py<br/>

8. python parser.py

9. python manage.py runserver
