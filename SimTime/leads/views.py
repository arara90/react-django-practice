from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_leads_items(request):
    print('leads views')
    return render(request, 'leads/leads_list.html')