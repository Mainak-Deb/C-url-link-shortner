from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout 

from django.contrib import messages
from django.utils import timezone
from math import ceil
# import the logging library
import logging
import json
from .models import Slink,Ulink,Clink,Contact

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
from django.http import HttpResponse


code=[]
for i in range(48,58):
    code.append(chr(i))
for i in range(65,91):
    code.append(chr(i))
for i in range(97,123):
    code.append(chr(i))



def home(request):
    return render(request,"index.html")
    #return HttpResponse("we are in home")
def short(request):
   try:
    if request.method=="POST":        
        l_name = request.POST.get('linksub', '')
        
        links = Slink( l_name=l_name)
        links.save()
        sid = links.l_id
        sid=int(sid)+5000;
        st=""
        for i in range(4):
                st=code[int(sid%62)]+st
                sid=sid//62
        st="127.0.0.1:8000/i/"+st
        return render(request, 'index.html', { 'id': st})
    
    return render(request, 'index.html')
   except:
       return render(request, 'error.html')

def search(request, lk):
  try:
   slk=str(lk)
   c=0;
   for i in range(3,-1,-1):
       k=int(code.index(slk[i]))
       c=c+(k*(62**(3-i)))
   c=c-5000;
   print(c)
   real_link = Slink.objects.filter(l_id=c)
  
   return HttpResponseRedirect(real_link[0].l_name)
  except:
      return render(request, 'error.html')

def insearch(request):
  try:
   if request.method=="POST":
        query= request.POST.get('isearch', '')
   query=query[-4:]
   slk2=str(query)
   c2=0;
   for i in range(3,-1,-1):
       k=int(code.index(slk2[i]))
       c2=c2+(k*(62**(3-i)))
   c2=c2-5000;
   print(c2);
   real_link = Slink.objects.filter(l_id=c2)
  
   return HttpResponseRedirect(real_link[0].l_name)
  except:
      return render(request, 'error.html')



def handleSignup(request):
    try:
        if request.method== "POST":
            #Get the post parameters
            username =request.POST['username']
            fname =request.POST['fname']
            lname =request.POST['lname']
            email =request.POST['email']
            pass1 =request.POST['pass1']
            pass2 =request.POST['pass2']

            #checks for erroneous inputs

            if (len(username)>10) :
                messages.error(request,"username must be under 10 characters")
                return redirect("home")

            #create the user
            if (pass1!=pass2) :
                messages.error(request,"password do not match")
                return redirect("home")

            #create the user        


            myuser= User.objects.create_user(username,email,pass1)
            myuser.first_name =fname
            myuser.last_name =lname
            myuser.save()
            messages.success(request,"Your Papyrus Account Has Been Succesfully Created, Please Login To Continue")
            return redirect("home")

        else:
            return render(request, 'error.html')
    except:
        return render(request, 'error.html')


def handleLogin(request):
	if request.method== "POST":
		#Get the post parameters
		loginusername =request.POST['loginusername']
		loginpassword =request.POST['loginpassword']	


		user =auth.authenticate(username=loginusername,password=loginpassword)

		if user is not None:
			auth.login(request,user)
			messages.success(request,"Succesfully logged In")
			return redirect("premium")

		else:
			messages.error(request,"Invalid Credentials")
			return redirect("premium")

	messages.error(request,"Please Signup Or Login to Continue")
	return redirect("home")


def handleLogout(request):
		logout(request)
		messages.success(request,"Succesfully logged Out")
		return redirect("home")


@login_required(login_url='handleLogin')
def premium(request):
    return render(request,"premium.html")

@login_required(login_url='handleLogin')
def pshort(request):
        try:
            if request.method=="POST":
                name = request.POST.get('name','')
                l_name = request.POST.get('linksub','')
                print(name,l_name)
                links = Ulink(name=name, l_name=l_name)
                links.save()
                sid = links.l_id
                sid=int(sid)+5000;
                st=""
                for i in range(4):
                    st=code[int(sid%62)]+st
                    sid=sid//62
                st="127.0.0.1:8000/j/"+st
                print(st)
                return render(request, 'premium.html', { 'id': st})
            else:
                return render(request, 'error.html')
        except:
            return render(request, 'error.html')
def psearch(request, lk):
  try:
   slk=str(lk)
   c=0;
   for i in range(3,-1,-1):
       k=int(code.index(slk[i]))
       c=c+(k*(62**(3-i)))
   c=c-5000;
   print(c)
   real_link = Ulink.objects.filter(l_id=c)
  
   return HttpResponseRedirect(real_link[0].l_name)
  except:
      return render(request, 'error.html')

def pinsearch(request):
  try:
   if request.method=="POST":
        query= request.POST.get('isearch', '')
   query=query[-4:]
   slk2=str(query)
   c2=0;
   for i in range(3,-1,-1):
       k=int(code.index(slk2[i]))
       c2=c2+(k*(62**(3-i)))
   c2=c2-5000;
   print(c2);
   real_link = Ulink.objects.filter(l_id=c2)
  
   return HttpResponseRedirect(real_link[0].l_name)
  except:
      return render(request, 'error.html')


@login_required(login_url='handleLogin')
def dashboard(request):
   try:
    name = request.GET.get('usertracker')
    print(request.user,type(request.user),name,type(name))
    print(str(request.user)==str(name))
    # updates=[]
    if(str(request.user)==str(name)):
        update = Ulink.objects.filter(name=name)
        # updates.append({'text': item.update_desc, 'time': item.timestamp,'Orders': item.items_json})
        links=[]
        count=0
        for i in update:
            count+=1 
            sid=i.l_id
            mlink=i.l_name
            print(sid,mlink)
            sid=int(sid)+5000;
            st=""
            for j in range(4):
                    st=code[int(sid%62)]+st
                    sid=sid//62
            st="127.0.0.1:8000/j/"+st
            links.append([count,st,mlink])
        print(links)
        table={"table":links}
        return render(request, 'dashboard_nrml.html',table)
    else:return render(request, 'error.html')
   except:
       return render(request, 'error.html')


@login_required(login_url='handleLogin')
def cshort(request):
   try:
    if request.method=="POST":
        name = request.POST.get('name','')
        l_name = request.POST.get('clinksub','')
        l_url = request.POST.get('curlnm','')
        print(name,l_url,l_name)
        check=Clink.objects.filter(l_url=l_url)
        print(len(check))  
        if(len(check)!=0):
            return render(request, 'premium.html',{ 'cu': "Link already exists, try another"})
        else:
            print("except")
            links = Clink(name=name, l_name=l_name,l_url=l_url)
            links.save()
            st="127.0.0.1:8000/c/"+str(l_url)
            return render(request, 'premium.html',{ 'cu': st})

    return render(request, 'premium.html')
   except:
       return render(request, 'error.html')

def csearch(request, lk):
  try:
   slk=str(lk)
   real_link = Clink.objects.filter(l_url=slk)
   return HttpResponseRedirect(real_link[0].l_name)
  except:
       return render(request, 'error.html')
 

def cinsearch(request):
  try:
   if request.method=="POST":
        query= request.POST.get('isearch', '')
   query=query[-4:]
   slk2=str(query)
   c2=0;
   for i in range(3,-1,-1):
       k=int(code.index(slk2[i]))
       c2=c2+(k*(62**(3-i)))
   c2=c2-5000;
   print(c2);
   real_link = Clink.objects.filter(l_id=c2)
   print(real_link)
   return HttpResponseRedirect(real_link[0].l_name)
  except:
      return render(request, 'error.html')
 



@login_required(login_url='handleLogin')
def customdashboard(request):
   try:
    name = request.GET.get('usertracker')
    print(request.user,type(request.user),name,type(name))
    print(str(request.user)==str(name))
    # updates=[]
    if(str(request.user)==str(name)):
        update = Clink.objects.filter(name=name)
        # updates.append({'text': item.update_desc, 'time': item.timestamp,'Orders': item.items_json})
        links=[]
        count=0
        for i in update:
            count+=1 
            print(i.l_url)
            mlink=i.l_name
            st="127.0.0.1:8000/c/"+str(i.l_url)
            links.append([count,st,mlink])
        print(links)
        table={"table":links}
        return render(request, 'custom_dashboard.html',table)
    else:
	    return render(request, 'error.html')
   except:
       return render(request, 'error.html')

def contact(request):
   try:
    if request.method=="POST":        
        mail= request.POST.get('mail', '')
        messege=request.POST.get('messege', '')
        sms = Contact( mail=mail,messege=messege)
        sms.save()
        messages.success(request,"Your messege send to our management team")
        return render(request,  'premium.html')
    return render(request,  'premium.html')
   except:
       return render(request, 'error.html')
