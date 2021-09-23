from django import forms
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StudentReg
from .models import User

# Create your views here.

# show data
def addShow(request):
    if request.method == 'POST':
        fm = StudentReg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentReg()
    else:
        fm = StudentReg()
    stud = User.objects.all()
    return render(request, "enroll/add_show.html", {'from': fm, 'std': stud})


# Update and Edit

def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentReg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
         pi=User.objects.get(pk=id)
         fm=StudentReg(instance=pi)

    return render(request, "enroll/updatedShow.html",{'form':fm})









# delete data
def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
