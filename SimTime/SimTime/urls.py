
from django.contrib import admin
from django.urls import path, include

print('urls.py')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls')),
    path('leads/', include('leads.urls')),
]
