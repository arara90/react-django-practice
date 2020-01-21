from rest_framework import routers
from .api import LeadViewSet

print('leads/url')

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
urlpatterns = router.urls  # 'api/leads'


# from . import views
# from django.urls import path, include
# urlpatterns = [
#     path('', views.list_leads_items),
# ]
