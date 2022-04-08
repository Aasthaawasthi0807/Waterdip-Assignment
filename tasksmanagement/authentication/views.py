from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , HttpResponseRedirect
from django.urls import reverse

from .forms import TaskRegistration
from .models import Task
# Create your views here.

#This Function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = TaskRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['title']
            em = fm.cleaned_data['description']
            st = fm.cleaned_data['status']
            reg = Task(title = nm, description = em,status=st)
            reg.save()
            #fm = TaskRegistration()
            return HttpResponseRedirect("/addandshow/")
           
    else:
        fm = TaskRegistration()
    stud = Task.objects.all()
    return render(request,"authentication/addandshow.html", {'form':fm, 'stu':stud })


#This function will update/edit
def update_data(request,id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=id)
        fm = TaskRegistration( request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Updated Task Detail Successfully!!')
    else:
        pi = Task.objects.get(pk=id)
        fm = TaskRegistration(instance=pi)

    return render(request,'authentication/update.html' , {'form':fm })


#This function will Delete
def delete_data(request , id):
    if request.method == 'POST':
        pi = Task.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
