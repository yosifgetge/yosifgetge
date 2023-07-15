from django.shortcuts import render
from .models import Login


def index(request):
    if request.method == 'POST':
     username = request.POST.get('username')
     password = request.POST.get('password')
     Active = request.POST.get('Active')
     datas = Login(username=username,password=password)
     datas.save()
     if datas.save() == True:
        print('Hello'+username)
    return render(request,'pages/index.html')
