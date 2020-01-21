참고 : https://www.youtube.com/watch?v=Nnoxz9JGdLU

참고 : [Django 기본 05 - Migration](https://wayhome25.github.io/django/2017/03/20/django-ep6-migrations/)



**postgresql 설치**

참고하기 : https://doorbw.tistory.com/183 [Tigercow.Door]

1. 다운로드

2. pip install psycopg2

   

**postgresql 확인**

postgresadmin에서 create -> DB -> todoDB 하나 생성



**장고에 연결정보 추가**

settings.py에 DB 정보 입력

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.porstgresql',
        'NAME': 'todoDB',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
    }
}


# =======================
# 내가 만든 app외에도 default로 제공된 app들이 있다.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'simtime_alpha',
    'todos',
]


```



**모델 정의**

app폴더 내 models.py에

```python
from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.TextField()
```



### DB 적용 명령어들

```
python manage.py makemigrations todos		# migration 파일 생성
python manage.py sqlmigrate todos 001		# 지정 migrations의 sql 확인하기
python manage.py migrate 					# execute in actualDB 
python manage.py showmigrations [app-name] 	# app별 migrations와 migrate 여부 ([X]:적용)
```



실습]

1. 기본 app들의 models 적용

   -> models.py에 작성한 부분 일단 주석처리하고 아래 코드를 실행해보자. (마지막코드만 실행)

   ```
   python manage.py migrate (app-name) [--DATABASE connectionName]
   ```



​	-> migrations 폴더에 __init__

​    -> postgresql admin -> schema -> table에장고 기본 앱에 필요한 table들 생성



2. models.py 주석처리 지우고 세개의 명령어 입력

   1. python manage.py makemigrations todos

      > 0001_initial 
   
   2. python manage.py sqlmigrate todos 0001 

```
BEGIN;
--
-- Create model Todo
--
CREATE TABLE "todos_todo" ("id" serial NOT NULL PRIMARY KEY, "content" text NOT NULL);
COMMIT;
```

3. python manage.py migrate ->  DB에 실제 반영되었다. schema -> tables 에 todos_todo 반영된 것 확인



### App router

1. project의 urls.js

   ```python
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('todos/', include('todos.urls')),
   ]
   ```

2. todos app 폴더내에 urls.py생성

   ```python
   from django.urls import path, include
   from . import views
   
   urlpatterns = [
       path('list/', views.list_todo_items),
   ]
   ```

3. views.py에 보여줄 페이지 연결

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   # Create your views here.
   def list_todo_items(request):
       return HttpResponse('from list_todo_items')
   ```
