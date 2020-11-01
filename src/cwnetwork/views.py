from django.shortcuts import render

def home_view(request):
    user = request.user
    data = "Hello"
    
    dic = {
        'user': user,
        'data': data,
    }
    return render(request,'main/home.html',dic)