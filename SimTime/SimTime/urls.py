
from django.contrib import admin
from django.urls import path, include

print('urls.py')
urlpatterns = [
    # 위에 있는 것이 우선순위 높다
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
    path('', include('frontend.urls')), 
    path('', include('leads.urls')),
    
]
