### Amazon RDS로 postgresql 만들기.



  PC 두 대로  작업할 예정이다. 작업 소스까지는 git으로 해도 DB 수정 내역까지 매번 새롭게 적용하는 게 불편할 것 같다. 내친김에 AWS로 postgresql을 써보자. 

[](https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html#USER_ConnectToPostgreSQLInstance.Troubleshooting)

Amazon RDS ->데이터베이스만들기-> postgresql 생성

프리티어를 사용할 예정이라 딱히 더 설정할 것도 없다.



##### 보안그룹 설정

 단, 로컬 pgAdmin에서 접근( [인스턴스 연결](https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html#USER_ConnectToPostgreSQLInstance.Troubleshooting) )할 때, 연결문제가 생기는데, 보안그룹 추가를 해줘야한다.

![pgAdmin](https://github.com/arara90/images/blob/master/Simtime/simtime%20000.png?raw=true)

```
not connect to server: Connection timed out.
```

[연결문제해결](https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html#USER_ConnectToPostgreSQLInstance.Troubleshooting) 참고하기.



다음과 같이 

1. 보안그룹 생성 
2. DB인스턴스 수정 -> 해당 그룹을 인스턴스에 추가, 퍼블릭액세스가능성 Yes해야  로컬 admin에서 접근할 수 있다. (database 목록 화면에서 해당 DB 선택 후 Modify버튼 클릭, **다른건 몰라도 UI는 진짜루 Azure의 완승이다!!!!!!! Azure 만세!!!!!!!**) 

(클라우드 기반의 빅데이터 전문가 과정에서 Azure로 매일했던 작업과 동일해서 수월하게 :D )

![](https://github.com/arara90/images/blob/master/Simtime/react%20001.png?raw=true)

 ![](https://github.com/arara90/images/blob/master/Simtime/react%20002.png?raw=true)



**짜란~ 연결 성공 !**

![](https://github.com/arara90/images/blob/master/Simtime/react%20003.png?raw=true)



이제 pgAdmin에서 todos를 만들고, settings.py의 host를 바꿔서 연결하면 된다.

```python
#settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todos',
        'USER': 'postgres',
        'PASSWORD': '비밀',
        'HOST': 'postgres-ara.c4kogceiqedh.us-east-2.rds.amazonaws.com', #endpoint
        'PORT': '5432'
    }
}
```

**짜란~ 연결 성공 !**

![](https://github.com/arara90/images/blob/master/Simtime/react%20004.png?raw=true)

![](https://github.com/arara90/images/blob/master/Simtime/react%20005.png?raw=true)



##### models.py

```python
#Create your models here.
class Todo(models.Model):
    content = models.TextField()
```



##### 적용해보기!

![](https://github.com/arara90/images/blob/master/Simtime/react%20006.png?raw=true)



##### 확인

![](https://github.com/arara90/images/blob/master/Simtime/react%20007.png?raw=true)



오예~ 드디어 작업 환경 설정이 모두 끝났다!



### 여러개 DB 연동하기

참고 : https://chohyeonkeun.github.io/2019/06/07/190607-django-multi-database/

​		   https://docs.djangoproject.com/en/2.1/topics/db/multi-db/

​		   https://hangpark.com/django-multi-db-relation/   ★★



1. ##### settings.py에 정보 입력

```python
DATABASES = {
    'default': {	#connectionsName
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todos',
        'USER': 'postgres',
        'PASSWORD': 'ㅇㅇㅇㅇ',
        'HOST': 'postgres-ara.c4kogceiqedh.us-east-2.rds.amazonaws.com', #endpoint
        'PORT': '5432'
    },
    'leads-db': {	#connectionsName
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'leads',
        'USER': 'postgres',
        'PASSWORD': 'ㅇㅇㅇㅇㅇ',
        'HOST': 'postgres-ara.c4kogceiqedh.us-east-2.rds.amazonaws.com', #endpoint
        'PORT': '5432'
    }
}
```



2. ##### settings.py에 db ROUTER 만들기

```python
DATABASE_ROUTERS = [
    # 라우터는 입력한 순서대로 실행된다. 
    #'path.to.Classname' #path.to는 실제 router파일이 저장된 위치
    # config 폴더 내 routers.py 파일의 MultiRouter Class
    'config.routers.MultiRouter',  

]
```



3. ##### router 파일 만들기 (프로젝트 폴더에)

   *  https://docs.djangoproject.com/en/2.1/topics/db/multi-db/ 참고해서 method별로 확인

```python
class MultiRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'leads':
            return 'leads-db' # db-connection명 return
        return 'default'

    def db_for_write(self,model,**hints):
        if model._meta.app_label == 'leads':
            return 'leads-db'
        return 'default'
    
    ...

```



4. **models.py 작성해보자**

```python
from django.db import models

# Create your models here.
class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
```



5. ##### makemigrations 명령어 결과 

   ![](https://github.com/arara90/images/blob/master/Simtime/react%20008.png?raw=true)

   

6. ##### DB 반영

* 자꾸 default에 저장되어 실패했다. -> routers.py 제대로 작성했는지 확인. 

  * 후에 allow_migrate에서 제어할 수 있었다.

    ```python
    class MultiRouter:
    	db_map = {
            'db-todos': 'todos'
        }
     	def allow_migrate(self, db, app_label, model_name=None, **hints):
            # print('here:                ', db, app_label, model_name)
            if (db in self.db_map.keys()):
                return app_label == self.db_map.get(db)
    
            else:
                return app_label not in self.db_map.values()
    ```

    

* [python manage.py makemigrations **leads**] : leads 앱의 migrations 저장

* [python manage.py migrate **leads** --DATABASE 'leads-db']  직접 명시하여 leads-db에 leads migrations내용 저장

  

* 쿼리에 직접 명시하기

```
>>> # This will run on the 'default' database.
>>> Author.objects.all()

>>> # So will this.
>>> Author.objects.using('default').all()

>>> # This will run on the 'other' database.
>>> Author.objects.using('other-db').all()
```


