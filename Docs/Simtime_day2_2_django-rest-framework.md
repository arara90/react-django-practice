# django REST framework

참고: https://www.youtube.com/watch?v=Uyei2iDA4Hs&t=641s (10:55)

https://www.django-rest-framework.org/



1. Serializers

   Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into `JSON`, `XML` or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.



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



```python
# api.py

from .models import Leads
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.using('leads').all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = LeadSerializer

```

* **Viewset** allows us to create a full CRUD api without having to specify explicit methods for the functionality



2. urls.py (app의 url)  => http://127.0.0.1:8000/leads/api/leads/

   ```python
   from rest_framework import routers
   from .api import LeadViewSet
   
   
   print('leads/url')
   
   router = routers.DefaultRouter()
   router.register('api/leads', LeadViewSet, 'leads')
   
   urlpatterns = router.urls #'api/leads'
   ```



3. 확인 

![html](https://github.com/arara90/images/blob/master/Simtime/simtime%20001.png?raw=true)

![pgadmin](https://github.com/arara90/images/blob/master/Simtime/simtime%20002.png?raw=true)

![postman](https://github.com/arara90/images/blob/master/Simtime/simtime%20001.png?raw=true)



GET : http://127.0.0.1:8000/leads/api/leads/2/ -> id가 2 인 data만 자동 검색





