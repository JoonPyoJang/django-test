from django.shortcuts import render
from .models import AccessLog

def test_introduce(request):
    if request.method == 'GET':
        logdata = AccessLog()
        logdata.location = "introduce page 접속"
        logdata.save()
        
    
    return render(request, 'main.html')
# Create your views here.
