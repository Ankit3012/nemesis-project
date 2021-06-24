from django.shortcuts import render
from .models import userlogin
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
# Create your views here.
import jwt
from time import time
# first we run the command in terminal for generate the private key:  ssh-keygen -t rsa -b 4096


def login(request):
    return render(request,'login.html')
def home(request,name):
    #in this user can go in home page while 5 mins
    private_key = open('jwt-key').read()
    f = open("publictoken.txt", "r")
    token3=f.read()

    payload = jwt.decode(token3, private_key, algorithms=['HS256'])
    if payload:

        nam = str(name)
        na = nam.capitalize()
        alldata = userlogin.objects.all()

        return render(request, 'home.html', {'name': na,
                                             'alldata': alldata
                                             })
    else:
        return render(request, 'login.html')
def regis(request):
    return render(request,'regis.html')
@csrf_exempt
def update(request):
    if request.method == 'POST':
        name = request.POST.get('user')
        email = request.POST.get('email')
        password = request.POST.get('email').password
        add = request.POST.get('add')
        print(name,email)
        post=userlogin(lname=name,email=email,password=password,ladd=add)
        post.save()
        return JsonResponse({'status':'save'},safe=False)
    else:return JsonResponse({'status': 0}, safe=False)

@csrf_exempt
def ser(request):

    if request.method == 'POST':
        man=request.POST.get('user')


        alldata = userlogin.objects.filter(email=man)

        serdata={'name': alldata[0].lname, 'email': alldata[0].email, 'add': alldata[0].ladd}



        return JsonResponse({'serial': serdata}, safe=False)
    else:print('error')
@csrf_exempt
def get(request):
    if request.method == 'POST':
        if request.POST.get('user'):
            post = userlogin()
            post.lname = request.POST.get('user')
            post.email = request.POST.get('email')
            post.password = request.POST.get('pass')
            post.ladd = request.POST.get('add')
            post.save()
            return JsonResponse({'status':'save'},safe=False)
    else:
        return JsonResponse({'status': 0}, safe=False)
def update(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            post = userlogin()
            post.lname = request.POST.get('user')
            post.email = request.POST.get('email')
            post.password = request.POST.get('pass')
            post.ladd = request.POST.get('add')
            post.save()
            return JsonResponse({'status':'save'},safe=False)
    else:
        return JsonResponse({'status': 0}, safe=False)
@csrf_exempt
def authen(request):
    if request.method == 'POST':
        if request.POST.get('user'):
            us=request.POST.get('user')
            pas = request.POST.get('pass')
            try:
                checku=userlogin.objects.filter(email=us)
                name=checku[0].lname
                checkp = checku[0].password
                if pas==checkp:
                    private_key = open('jwt-key').read()
                    token3 = jwt.encode({

                        'user_id': 'H125-f115-T548',
                        'username': 'ankit gupta',
                        'roles': ['user', 'moderator'],
                        'exp': time() + 300}, private_key, algorithm='HS256')
                    f = open("publictoken.txt", "w")
                    f.write(token3)
                    f.close()
                    print(token3)
                    return JsonResponse({'status': 'save','emp':name}, safe=False)
                else:
                    return JsonResponse({'status': 2}, safe=False)
            except:
                return JsonResponse({'status': 0}, safe=False)

        else:
            return JsonResponse({'status': 500}, safe=False)
    else:
        return JsonResponse({'status': 0}, safe=False)