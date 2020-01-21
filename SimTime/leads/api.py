from .models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    # print('Viewset class')
    # queryset = Lead.objects.all()
    # permission_classes = [
    #     permissions.AllowAny
    # ]

    permission_classes = [
        permissions.IsAuthenticated

    ]

    serializer_class = LeadSerializer

    def get_queryset(self):
        # It's gonna get only the leads of that user
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
