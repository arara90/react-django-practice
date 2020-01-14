from .models import Leads
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    print('Viewset class')
    queryset = Leads.objects.using('leads').all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = LeadSerializer