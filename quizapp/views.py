from django.shortcuts import render
from . models import Account
from django.core.exceptions import ObjectDoesNotExist
import time

# Create your views here.
def index(request):
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request,"index.html",{'name':name})
     except ObjectDoesNotExist:
          return render(request,"index.html")
def registration(request):
     return render(request,"registration.html")
def cusernam(request):
     name = request.POST['name']
     gender = request.POST['gender']
     address = request.POST['address']
     contactno = request.POST['contactno']
     emailaddress = request.POST['emailaddress']
     uname = request.POST['uname']
     password = request.POST['password']
     ac = Account(name=name, gender=gender, address=address, contactno=contactno, emailaddress=emailaddress,uname=uname, password=password)
     ac.save()
     return render(request,"rsucess.html")
def login(request):
     return render(request,"login.html")
def logcode(request):
     msg1=''
     uname=request.POST['uname']
     password=request.POST['password']
     try:
          obj=Account.objects.get(uname=uname,password=password)
          name=obj.name
          request.session['name']=name
          return render(request,"index.html",{'name':name})
     except ObjectDoesNotExist:
          msg1='Invalid username or password'
          return render(request,"login.html",{'msg1':msg1})
def logout(request):
     request.session['name'] =None
     return render(request,"index.html")
def gkquiz(request):
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request,"gkquiz.html",{'name':name})
     except ObjectDoesNotExist:
          msg='Please login'
          return render(request,"index.html",{'msg':msg})
def mathquiz(request):
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request,"mathquiz.html",{'name':name})
     except ObjectDoesNotExist:
          msg='Please login'
          return render(request,"index.html",{'msg':msg})
def sciencequiz(request):
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request,"sciencequiz.html",{'name':name})
     except ObjectDoesNotExist:
          msg='Please login'
          return render(request,"index.html",{'msg':msg})
def computerquiz(request):
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request,"computerquiz.html",{'name':name})
     except ObjectDoesNotExist:
          msg='Please login'
          return render(request,"index.html",{'msg':msg})
def gkqresult(request):
     ans1,ans2,ans3,ans4,ans5=0,0,0,0,0
     if (request.POST['a5']=='c'):
          ans1=1
     if (request.POST['a2']=='d'):
          ans2 = 1
     if (request.POST['a3']=='b'):
          ans3 = 1
     if (request.POST['a4']=='d'):
          ans4 = 1
     if (request.POST['a5']=='c'):
          ans5 = 1
     msg='You have scored = '+str(ans1+ans2+ans3+ans4+ans5)
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request, "gkquiz.html", {'name': name,'msg':msg})
     except ObjectDoesNotExist:
          return render(request, "gkquiz.html",{'msg':msg})
def mqresult(request):
     ans1,ans2,ans3,ans4,ans5=0,0,0,0,0

     if (request.POST['a1']=='a'):
          ans1=1
     if (request.POST['a2']=='c'):
          ans2 = 1
     if (request.POST['a3']=='b'):
          ans3 = 1
     if (request.POST['a4']=='c'):
          ans4 = 1
     if (request.POST['a5']=='d'):
          ans5 = 1
     msg = 'You have scored = ' + str(ans1 + ans2 + ans3 + ans4 + ans5)
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request, "mathquiz.html", {'name': name, 'msg': msg})
     except ObjectDoesNotExist:
          return render(request, "mathquiz.html", {'msg': msg})
def cqresult(request):
     ans1, ans2, ans3, ans4, ans5 = 0,0,0,0,0
     if (request.POST['a5']=='c'):
          ans1=1
     if (request.POST['a2']=='a'):
          ans2 = 1
     if (request.POST['a3']=='b'):
          ans3 = 1
     if (request.POST['a4']=='c'):
          ans4 = 1
     if (request.POST['a5']=='a'):
          ans5 = 1
     msg = 'You have scored = ' + str(ans1 + ans2 + ans3 + ans4 + ans5)
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request, "computerquiz.html", {'name': name, 'msg': msg})
     except ObjectDoesNotExist:
          return render(request, "computerquiz.html", {'msg': msg})
def sqresult(request):
     ans1,ans2,ans3,ans4,ans5= 0,0,0,0,0
     if (request.POST['a5']=='d'):
          ans1=1
     if (request.POST['a2']=='b'):
          ans2 = 1
     if (request.POST['a3']=='d'):
          ans3 = 1
     if (request.POST['a4']=='d'):
          ans4 = 1
     if (request.POST['a5']=='a'):
          ans5 = 1
     msg = 'You have scored = ' + str(ans1 + ans2 + ans3 + ans4 + ans5)
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request, "sciencequiz.html", {'name': name, 'msg': msg})
     except ObjectDoesNotExist:
          return render(request, "sciencequiz.html", {'msg': msg})
def contactus(request):
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request,"contactus.html",{'name':name})
     except ObjectDoesNotExist:
          return render(request,"contactus.html")
def aboutus(request):
     try:
          obj = Account.objects.get(name=request.session['name'])
          name = obj.name
          return render(request,"aboutus.html",{'name':name})
     except ObjectDoesNotExist:
          return render(request,"aboutus.html")