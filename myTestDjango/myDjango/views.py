from django.shortcuts import render
import re
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')
def comment(request):
    username = request.POST.get('username')
    comment = request.POST.get('password')
    #if re.match('^[0-9a-z/A-Z/n,.!?()"]+$',comment):
    if username != '':
        if comment != '':
            user = User()
            user.username = username
            user.comment = comment
            user.save()
            return render(request,'success.html')
        else:
            return render(request,'fail.html')
    else:
        return render(request,'fail.html')
    #else:
     #   return render(request,'fail.html')
def video1(request):
    return render(request,'video1.html')
def video2(request):
    return render(request,'video2.html')
def video3(request):
    return render(request,'video3.html')
def fail(request):
    return render(request, 'index.html')