from django.urls import path, include
from . import views

print('leads/url')
urlpatterns = [
    path('', views.list_leads_items),
]
