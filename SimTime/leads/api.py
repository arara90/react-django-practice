from leads.models import Leads
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset
class LeadViewSets(viewsets.modelViewSet):
    queryset = Leads.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = LeadSerializer