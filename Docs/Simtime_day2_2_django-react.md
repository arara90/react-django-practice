### Amazon RDS로 postgresql 만들기.



 PC 두 대로 왔다갔다 작업할 예정이다. 작업 소스까지는 git으로 해도 DB 수정 내역까지 매번 새롭게 적용하는 게 불편할 것 같다. 내친김에 AWS를 써보자. 

[](https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html#USER_ConnectToPostgreSQLInstance.Troubleshooting)

Amazon RDS ->데이터베이스만들기-> postgresql 생성

프리티어를 사용할 예정이라 딱히 더 설정할 것도 없다.



 단, 로컬 pgAdmin에서 접근( [인스턴스 연결](https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html#USER_ConnectToPostgreSQLInstance.Troubleshooting) )할 때, 연결문제가 생기는데, 보안그룹 추가를 해줘야한다.

![pgAdmin](https://github.com/arara90/images/blob/master/Simtime/simtime%20000.png?raw=true)

```
not connect to server: Connection timed out.
```

[연결문제해결](https://docs.aws.amazon.com/ko_kr/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html#USER_ConnectToPostgreSQLInstance.Troubleshooting) 참고하기.



다음과 같이 

1. 보안그룹 생성 
2. DB인스턴스 수정 -> 해당 그룹을 인스턴스에 추가, 퍼블릭액세스가능성 Yes해야  로컬 admin에서 접근할 수 있다. 

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



models.py

```python
#Create your models here.
class Todo(models.Model):
    content = models.TextField()
```



적용해보기!

![](https://github.com/arara90/images/blob/master/Simtime/react%20006.png?raw=true)



확인

![](https://github.com/arara90/images/blob/master/Simtime/react%200076.png?raw=true)



오예~ 드디어 작업 환경 설정이 모두 끝났다!

