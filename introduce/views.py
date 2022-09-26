from django.shortcuts import render

def test_introduce(request):
    return render(request, 'main.html')
# Create your views here.
