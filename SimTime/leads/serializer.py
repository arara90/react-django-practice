from rest_Framework import serializers
from leads.models import Leads

#L Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__' 