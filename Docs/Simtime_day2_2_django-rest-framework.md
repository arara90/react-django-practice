# django REST framework

참고: 	https://www.youtube.com/watch?v=Uyei2iDA4Hs&t=641s (10:55)

​			 https://jamanbbo.tistory.com/43 ★★★★

​			 https://www.django-rest-framework.org/

번역 	https://kimdoky.github.io/django/2018/07/11/drf-Serializers/

​            http://raccoonyy.github.io/tag/django-rest-framework-3/index.html ★★★★



### REST 

Web에서 데이터를 주고받는 규약.

HTTP 기본메서드 4가지 POST, GET, PUT, DELETE 를 통해 컨벤션을 유지한다면 RESTful 하다고 한다.

(PUT: 데이터 전체 변경(미입력 데이터는 NULL로 바꿈) / PATCH: 일부 변경)



### Serializers

Serializers allow **complex data** such as querysets and model instances **to be converted to native Python datatypes** that can then be easily rendered into `JSON`, `XML` or other content types. Serializers **also provide deserialization**, allowing **parsed data to be converted back into complex types, after first validating the incoming data.**

즉, serializations은 복잡한 데이터를 다른 네트워크 환경과의 통신을 위해 전송가능한 형태로 변환하는 것. 보통 byte로 쪼갠후 줄줄이 보낸다 / ex. json(or python 기본 자료형)->byte) 그 반대가 deSerializtion. (byte->json(or python 기본 자료형)

이를 python에서는 rest_framework의 serializers가 담당한다.



> ### JSON 변환과정
>
> 이제 이 Serializer를 불러와서 JSON으로 반환해주자
>
> ```
> views.py
> from .serializers import PetSerializer
> 
> def getPet(request):
>   pet = Pet.objects.get(pk=1)
>   serializer = PetSerializer( pet )
> ```
>
> _id가 1인 펫을 QuerySet 이라는 복잡한 Django type에서 Python의 Dictionary로 변환하였다
>
> 이제 이것을 전송하기 위해 문자열로 변환해주자
>
> ```python
> from .serializers import PetSerializer
> from rest_framework.renderers import JSONRenderer
> from django.http import HttpResponse
> 
> def getPet(request):
>       pet = Pet.objects.get(pk=1)
>       serializer = PetSerializer(pet)
>       data = JSONRenderer().render(serializer.data)
>       return HttpResponse(data)
> ```
>
> 참고 : https://velog.io/@ground4ekd/django-rest-framework



#### Serializers.py

```python
# Serializers.py

from rest_framework import serializers
from leads.models import Leads

#L Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__' 

```

####  api.py

```python
from .models import Leads
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.using('leads-db').all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = LeadSerializer

```

* **Viewset** allows us to create a full CRUD api without having to specify explicit methods for the functionality. 
* 즉, 자주 사용하는 공통적인 view로직(CRUD)을 그룹화하여 viewset으로 제공. 



#### leads > urls.py (app의 url)  

```python
from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
#(url-prefix, viewSet)

urlpatterns = router.urls #http://127.0.0.1:8000/leads/api/leads/
 # http://127.0.0.1:8000/api/leads/로 테스트하는게 좋다. 
 # 나는 프로젝트 url에서 leads 패턴으로 router했기때문에 leads가 더 있다.
```

* viewset을 router에 연결하면 자동으로 url맵핑. 

  ```
  URL pattern: ^api/leads/$ Name: 'movie-list'
  URL pattern: ^api/leads/{pk}/$ Name: 'movie-detail'
  ```

* 즉, view.py에 CRUD를 각각 연결해줬던 것을 더이상 하지 않아도 된다.

* [뷰셋과 주소를 명시적으로 연결하기](http://raccoonyy.github.io/drf3-tutorial-6/)



#### 확인 

![html](https://github.com/arara90/images/blob/master/Simtime/simtime%20001.png?raw=true)

![pgadmin](https://github.com/arara90/images/blob/master/Simtime/simtime%20002.png?raw=true)

![postman](https://github.com/arara90/images/blob/master/Simtime/simtime%20001.png?raw=true)

* GET : http://127.0.0.1:8000/leads/api/leads/2/ -> id가 2 인 data만 자동 검색



api 요청 uri - method

GET /leads/		 		  leads리스트 조회

POST /leads/ 				leads객체 추가

GET /leads/{pk}/ 		 leads객체 조회 .(한개)

PUT /leads/{pk} 		  leads객체 수정

DELETE /leads/{pk} 	leads객체 삭제

출처: https://jamanbbo.tistory.com/43 [자기계발하는 쏭이]

