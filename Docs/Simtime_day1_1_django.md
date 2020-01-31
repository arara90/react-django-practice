### Django 프로젝트 만들기..기억을 되살리자..

pip3 install pipenv

pipenv shell 			> create virtualen  .. pipfile 생성됨)  pipenv로 터미널 변경

code . 

```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]

[requires]
python_version = "3.7"
```

pipenv install django djangorestframework django-rest-knox ->(Pipfile.lock 생성)



django-admin startproject leadmanager -> leadmanager폴더 생성



장고프로젝트생성

django-admin startproject leadmanager

-> leadmanger폴더와 manage.py 생성



앱 생성

cd .\leadmanager\       

python manage.py startapp leads



settings.py로 이동해서  app등록 (simtime, rest_framework)

```
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'simtime',
'rest_framework'
]
```



### 무엇을 언제 써야할까? nodeJS vs Django by 노마드코더

**장고** -> CRUD / 블로그, 유투브, 인스타그램

 **nodeJS** -> 리얼타임, API-자바스크립트 BASE, 커스터마이징이 많을 때 /우버, 넷플릭스(스트리밍, 리얼타임 )

즉, 장고는 박스에 필요한 것만 남기는 작업 / nodeJS는 빈 곳에 레고를 쌓듯이 차곡차곡 



> 심탐이는  Django로 결정.  일정을 CRUD하는 작업이 많이 있을 것이니까. 또 nodeJS는 Amailie를 통해 접해 볼 기회가 생길 예정임.



### 모듈번들러 -> 웹팩, Parcel

: 여러개로 나뉜 파일들을 하나의 파일로 만들어줌

-> 이전, 나누어진 파일을 보여주기 위해 여러번 통신, 모듈 개념이 없을때는 파일 나뉘어져있어도 변수 스코프 생각해 개발.

-> 최신 js 모듈개념이 생겼지만 지원 X 브라우저들을 위해 지원 코드로 변환 필요



즉, 

1. 여러개의 자바스크립트 파일을 하나의 파일로 묶어 한번에 요청 -> 압축, 최적화 통해 로딩 속도

2. 최신 JS문법을 브라우저에서 사용하도록 변환 

3. 초기 로딩 속도 느린것을 보완하기 위해서 -> 청크, 캐시, 코드스플릿 개념 도입



### PostgreSQL vs MongoDB

-> mySQL은 Amailie에서 쓰기도하고,,,  데이터 관련 업무를 꼭 해보고 싶기 때문에 noSQL 종류를 새롭게 써보고 싶었다. 게다가 react 수업 들을 때 mongoDB를 썼기때문에 Django+MongoDB를 찾아봤으나 django와 postgresql이 최적. 안정적인 ORM을 지원하기 때문일까? (mongo도 불가능한 것은 아니다. [참고](https://django-mongodb-engine.readthedocs.io/en/latest/index.html))  

 하지만 Postgresql은 NoSQL 아니라는 것에 좌절..했지만 postgresql도 JSON 형식을 지원하니 일단 하이브리드 느낌으로 사용해보겠다. (라고 썼지만 혼자 엄청 헤매고 고민함ㅋㅋㅋ) 일단 Simtime 완성을 목표로 서비스 구현을 완성하면, 2차 과제로 postgresql에 있는 데이터도 mongodb로 migration해보고, 레알 하이브리드로 병행 운영해봐야지..

(데이터 업무에 대한 미련으로 NoSQL을 끝까지 놓지 못하는 자...)



왜일까? django의 contrib.postgresql 지원. 

> ## MongoDB와 PostgreSQL의 차이점
>
> 데이터베이스 시스템에서 두 가지 [많이 사용되는](https://insights.stackoverflow.com/survey/2019#technology-_-databases) 것은 [MongoDB](https://www.mongodb.com/what-is-mongodb)와 [PostgreSQL](https://www.postgresql.org/about/)입니다.
>
> MongoDB는 JSON을 사용하고 스키마 없는 데이터를 저장하도록 고안된 NoSQL 문서 데이터베이스입니다. 유연한 비정형 데이터, 실시간 분석 캐싱 및 수평적 크기 조정에 적합합니다.
>
> PostgreSQL(Postgres라고도 함)은 확장성 및 표준 준수에 중점을 둔 SQL 관계형 데이터베이스입니다. 이제 JSON도 처리할 수 있지만, 일반적으로 정형 데이터, 수평적 크기 조정 및 전자 상거래 및 금융 거래와 같은 ACID 호환 요구에 더 적합합니다.
>
> 스키마:
>
> **PostgreSQL:** 테이블 | 열 | 값 | 레코드
>
> **MongoDB(NoSQL):** 컬렉션 | 키 | 값 | 문서
>
> 선택한 데이터베이스의 종류는 데이터베이스와 함께 사용하는 애플리케이션의 유형에 따라 달라집니다. 정형 및 비정형 데이터베이스의 장점과 단점을 살펴보고 사용 사례에 따라 선택하는 것이 좋습니다. PostgreSQL 및 MongoDB 외에도 몇 가지 다른 데이터베이스 시스템을 고려해야 합니다.
>
>  참고
>
> 사용 중인 프레임워크 및 도구를 특정 데이터베이스 시스템에 통합하는 방법을 고려해야 할 수도 있습니다. [Django 웹 프레임워크](https://docs.microsoft.com/ko-kr/windows/python/web-frameworks#hello-world-tutorial-for-django)는 PostgreSQL와 더 잘 통합될 수 있습니다([Django 문서](https://docs.djangoproject.com/en/2.2/ref/contrib/postgres/) 및 [psycopg2](https://github.com/psycopg/psycopg2) 참조). [Flask 웹 프레임워크](https://docs.microsoft.com/ko-kr/windows/python/web-frameworks#hello-world-tutorial-for-flask)는 MongoDB와 더 잘 통합될 수 있습니다([MongoEngine](https://github.com/MongoEngine/flask-mongoengine) 및 [PyMongo](https://github.com/dcrosta/flask-pymongo) 참조).

**참고** https://pynative.com/python-postgresql-tutorial/





이렇게 나의 심탐이는 

React

Django

PostgreSQL



====> 호오 <====

#### [Instagram Stack](http://stackshare.io/instagram/instagram)

본 Full Stack은 [Instagram](https://instagram.com/)의 [Pete Hunt](https://github.com/petehunt)가 발표했던 [Instagram에서 React를 통해 SPA를 도입한 사례 소개 영상](https://youtu.be/VkTCL6Nqm6Y) 의 영향을 받았고 Instagram 관련 기술 정보 들을 많이 참고하여 만들어 졌습니다. Instagram에서 적극적으로 정보를 공유해주어 참고할 수 있는 자료가 많았는데요, 개발팀이 스타트업 초기 고려했던 기술 스택에 대해 쓴 글인 [**'What Powers Instagram: Hundreds of Instances, Dozens of Technologies'**](http://instagram-engineering.tumblr.com/post/13649370142/what-powers-instagram-hundreds-of-instances)은 [한글로 번역된 포스팅](https://charsyam.wordpress.com/2011/12/17/발-번역-수백대의-장비와-수십가지의-기술-instagram의-힘/)도 존재합니다. 결국 본 데모 프로그램에 사용한 주요 기술들인 React+Django+PostgreSQL 은 Instagram 과 정확히 일치합니다.

http://webframeworks.kr/tutorials/react/react-django-full-stack-spa/



 

+ 후에 AWS로 올리기 