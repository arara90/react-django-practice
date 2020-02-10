# Django Token Authentication

* 유투브 강의 : [Traversy Media - Full Stack React & Django [5] - Django Token Authentication](https://youtu.be/0d7cIfiydAc?list=PLillGF-RfqbbRA-CIUxlxkUpbq0IFkX60)



> ![connectionError](https://github.com/arara90/images/blob/master/Simtime/simtime%20032.png?raw=true)
>
> migrate --DATABASE 뒤에 붙이는 것은 db-name이 아니라 settings.py에서 지정한 DATABASE의 key값, 즉 connection name임을 알 수 있다.



### CRUD를 위한 Authentication

* **leads > models.py**

```python
from django.contrib.auth.models import User
owner = models.ForeignKey(User, related_name="leads", on_delete=models.CASCADE, null=TRUE)
```



* **leads > api.py**

```python
from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

class LeadViewSet(viewsets.ModelViewSet):
    # queryset = Lead.objects.all()
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = LeadSerializer

    def get_queryset(self):
        # 해당 유저의 leads만 return한다.
        return self.request.user.leads.all()
    
    def perform_create(self, serializer):
        #lead를 만들때 owner를 저장하도록 한다.
        serializer.save(owner=self.request.user)


```

dev tool로 확인하면, 403 Error (Forbidden)발생. Error에 state를 넣어 더 자세하게 작성해볼까?.



* **frontend > src > actions > messages.js **

  ```
  // RETURN ERRORS
  export const returnErrors = (msg, status) => {
    return {
      type: GET_ERRORS,
      payload: { msg, status }
    };
  };
  ```

  

* **frontend > src > actions > leads.js **

  ```python
  import { createMessage, returnErrors } from "./messages";
  
  //...
  
  // GET LEADS
  export const getLeads = () => dispatch => {
    axios
      .get("/api/leads/")
      .then(res => {
        // pass in an object with a type
        dispatch({
          type: GET_LEADS,
          payload: res.data
        });
      })
      .catch(err =>
        #요기에 status를 담자. 
        dispatch(returnErrors(ㄷrr.response.data, err.response.status))
      );
  };
  
  
  // ADD LEAD
  export const addLead = lead => dispatch => {
    axios
      .post(`/api/leads/`, lead)
      .then(res => {
        // pass in an object with a type
        dispatch({
          type: ADD_LEAD,
          payload: res.data
        });
  
        dispatch(createMessage({ addLead: "Lead Added" }));
      })
      .catch(err => {
        // const errors = {
        //   msg: err.response.data,
        //   status: err.response.status
        // };
  
        // dispatch({
        //   type: GET_ERRORS,
        //   payload: errors
        // });
        // 다음으로 변경
        dispatch(returnErrors(err.response.data, err.response.status));
      });
  };
  
  ```



![authError](https://github.com/arara90/images/blob/master/Simtime/simtime%20033.png?raw=true)





### Authentication

##### restistration API를 생성 -> User 등록하기 

 login API 생성 -> login 



### Token

* User 등록 시 header에 token을 담아 보낼 수 있음 -> 이를 authentication에 활용하여 사용자를 인식함.

#### django-knox 

* **setting.py** 에 등록하기

```
INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'rest_framework',
      'leads',
      'todos',
      'frontend',
      'knox'
  ]

  ...
  
REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES':
      ('knox.auth.TokenAuthentication', ) # Tuple에서 ,를 제외하면 string으로 인식한다.
}





```

  그리고 python manage.py migrate

  

* **accounts 앱 만들고 serializers.py 생성하기**

  python manage.py startapp accounts



* **accounts > serializers.py**

```python
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('id', 'username', 'email')

# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        user = User.objects.create_user(
            validate_Data['username'], validate_Data['email'], validate_Data['password']
        )
        return user


# Login Serializer
```

**validate_data** : To make sure it's the right type of data following the structure of a User model which we didn't create (that's included with django)



#### RegisterAPI

* **accounts > api.py**

  ```python
  from rest_framework import generics, permissions
  from rest_framework.response import Response
  from knox.models import AuthToken
  from .serializers import UserSerializer, RegisterSerializer
  
  # Register API
  
  
  class RegisterAPI(generics.GenericAPIView):
      serializer_class = RegisterSerializer
  
      def post(self, request, *args, **kwargs):
          serializer = self.get_serializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          user = serializer.save()
  
          # response back
          return Response({
              "user": UserSerializer(user, context=self.get_serializer_context()).data,
              # Token은 Header에 담겨서 user를 식별함
              "token": AuthToken.objects.create(user)[1]
          })
  # Login API
  
  
  # Get User API
  
  ```

  > **Error : Object of type 'AuthToken' is not JSON serializable **
  >
  > ```python
  > #api.py
  > "token": AuthToken.objects.create(user)
  > ```
  >
  > * Tuple을 return하기 때문에 AuthToken.objects.create(user)[1] 로 수정.  혹은 아래와 같이.
  >
  >   ```python
  >    [_, token] = AuthToken.objects.create(user)  # Tuple을 return하기 때문에
  >           # response back
  >           return Response({
  >               "user": UserSerializer(
  >                   user,  # pass user object
  >                   context=self.get_serializer_context()
  >               ).data,
  >   
  >               # Token은 Header에 담기게되고, 이를 활용해서 user를 식별,인증함
  >               "token": token
  >           })
  >       
  >   
  >   ```
  >
  >   * **실제 AuthToken.objects.create(user)의 return 값**   
  >
  >   (<AuthToken: 9092833f4e4c55b7348effe983f77998405d5432cd47cd8d30668b4c19eff8b13e1f415a032bcec322a2e1fafb9d2a95a802f39d0a10d1840be2f6a823fe2f21 : dfdsf1sf>, '216de856312bc3f6c3de0a879d4ac2846919efa02b15d6ddeac27a22d960f49b')



* **urls.py**

  ```python
  from django.urls import path, include
  from .api from RegisterAPI
  from knox import views as knox_views
  
  urlpatters = [
      path('api/auth', include('knox.urls')),
      path('api/auth/register', RegisterAPI.as_view())
  ]
  ```



* **project root > urls.py**

  ```python

  from django.contrib import admin
  from django.urls import path, include
  
  print('urls.py')
  urlpatterns = [
      # 위에 있는 것이 우선순위 높다
      path('admin/', admin.site.urls),
      path('todos/', include('todos.urls')),
      path('', include('frontend.urls')),
      path('', include('leads.urls')),
      path('', include('accounts.urls')), #추가
  
  ]
  
  ```
  



#### 결과

Request-Response

![result](https://github.com/arara90/images/blob/master/Simtime/simtime%20038.png?raw=true)



Header

![Content-Type](https://github.com/arara90/images/blob/master/Simtime/simtime%20039.png?raw=true)

