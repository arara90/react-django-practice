# Django Token Authentication 2 

* 유투브 강의 : [Traversy Media - Full Stack React & Django [5] - Django Token Authentication](https://youtu.be/0d7cIfiydAc?list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60)



### Authentication : Login

restistration API를 생성 -> User 등록하기 

#####  login API 생성 -> login  -> token 발행

> 1. knox 앱 등록
> 2. **serializer 작성**
> 3. **api 작성**
> 4. **urls 등록** 



#### Serializer

```python
# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

```



#### API

```python
# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        [_, token] = AuthToken.objects.create(user)  # Tuple을 return하기 때문에

        # response back
        return Response({
            "user": UserSerializer(
                user,  # pass user object
                context=self.get_serializer_context()
            ).data,

            # Token은 Header에 담기게되고, 이를 활용해서 user를 식별,인증함
            "token": token
        })

```



#### urls

```python
from django.urls import path, include
from .api import RegisterAPI,LoginAPI
from knox import views as knox_views

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view())
]
```



#### 결과

* ##### Incorrect

![incorrect](https://github.com/arara90/images/blob/master/Simtime/simtime%20035.png?raw=true)

![Content-Type](https://github.com/arara90/images/blob/master/Simtime/simtime%20039.png?raw=true)



* ##### Correct

![correct](https://github.com/arara90/images/blob/master/Simtime/simtime%20036.png?raw=true)





### Authentication : get User

#### api.py

* **permission_classes** : we want this route to be protected, meaning **It needs to have a valid token**

  -> need to be logged in to be able to access.

* **self.request.user** :  token을 확인하고 해당하는 user를 return 한다.

```python
# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
```



#### urls.py

```python
# 추가
path('api/auth/user', UserAPI.as_view()) 
```



#### 결과

Header에 token 정보를 담아 get 요청을 보내면, 해당 token에 맞는 user 정보가 Response에 담겨 온다.

> KEY : Authorization
>
> VALUE: Token [token 문자열]

![correct](https://github.com/arara90/images/blob/master/Simtime/simtime%20040.png?raw=true)



### Authentication : Logout

#### urls.py

```python
 path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
```

* token을 invalidate한다.



#### 결과

![logout](https://github.com/arara90/images/blob/master/Simtime/simtime%20041.png?raw=true)

* Token을 담아 logout

![invalidToken](https://github.com/arara90/images/blob/master/Simtime/simtime%20042.png?raw=true)

* 해당 token이 invalid한 것을 확인할 수 있다.