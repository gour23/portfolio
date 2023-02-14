from django.shortcuts import render,HttpResponse , redirect
from myAppp.models import Work , Contact
from django.contrib import messages
import re


# Create your views here.
def home(request):
    return render(request,'front.html')

def work(request):
    works = Work.objects.all()
    context = {"works":works}
    return render(request,'mywork.html' , context)

def workposts(request,slug):
    work = Work.objects.filter(slug=slug).first()
    context = {"work":work}
    return render(request,'workposts.html' , context)

def achievments(request):

    return render(request,'achievments.html')

def contact(request):
    if request.method ==  'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        content = request.POST.get("content")

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        # if re.fullmatch(regex,email):


        if len(name)==0 :
            messages.error(request,' Ooops , Name is missed , Please Enter the Name !! ')
            return redirect('contact')
        elif len(email)==0:
            messages.error(request,'Ooops , Email is missed , Please Enter the Email !!')
            return redirect('contact')
        elif len(phone)==0:
            messages.error(request,'Ooops , Phone Number is missed , Please Enter the Phone Number!! ')
            return redirect('contact')

        elif re.fullmatch(regex,email):
            instance =Contact(name=name, phone=phone,email=email,content=content)
            instance.save()
            messages.info(request, 'Your Form is Submitted , Thank You!!')
        else:
            messages.error(request,'Please Enter valid email Id ')
            return redirect('contact')
    
    
    return render(request,'contact.html')