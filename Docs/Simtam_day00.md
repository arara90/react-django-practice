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



settings.py로 이동해서 

```
INSTALLED_APPS = [
'simtime_alpha',
'rest_framework'
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',

]
```



### 무엇을 언제 써야할까? nodeJS vs Django by 노마드코더

**장고** -> CRUD / 블로그, 유투브, 인스타그램

 **nodeJS** -> 리얼타임, API-자바스크립트 BASE, 커스터마이징이 많을 때 /우버, 넷플릭스(스트리밍, 리얼타임 )



즉, 장고는 박스에 필요한 것만 남기는 작업 / nodeJS는 빈 곳에 레고를 쌓듯이 차곡차곡 



> 심탐이는  Django로 결정.  일정을 CRUD하는 작업이 많이 있을 것이니까. 또 nodeJS는 Amailie를 통해 접해 볼 기회가 생길 예정임.



### 모듈번들러 -> 웹팩, PArcel

: 여러개로 나뉜 파일들을 하나의 파일로 만들어줌

-> 이전, 나누어진 파일을 보여주기 위해 여러번 통신, 모듈 개념이 없을때는 파일 나뉘어져있어도 변수 스코프 생각해 개발.

-> 최신 js 모듈개념이 생겼지만 지원 X 브라우저들을 위해 지원 코드로 변환 필요



즉, 

1. 여러개의 자바스크립트 파일을 하나의 파일로 묶어 한번에 요청 -> 압축, 최적화 통해 로딩 속도

2. 최신 JS문법을 브라우저에서 사용하도록 변환 

3. 초기 로딩 속도 느린것을 보완하기 위해서 -> 청크, 캐시, 코드스플릿 개념 도입

#### 



### PostgreSQL vs MongoDB

-> mySQL은 Amailie에서 쓰기도하고,,,  데이터 관련 업무를 꼭 해보고 싶기 때문에 noSQL 종류를 새롭게 써보고 싶었음. 

-> react 수업 들을 때 mongoDB를 썼기때문에 Django+MongoDB를 찾아봤으나 추천하지 않음.. 차라리 flask를 쓰래. 자료도 몇 없음 PostgreSQL 얘기가 많길래 찾아봤더니 PostgreSQL + Django는 또 많이 나옴. 

​	왜일까?

> PostgreSQL로 하자.

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