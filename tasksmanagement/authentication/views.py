from asyncio import all_tasks
from turtle import title
from django.contrib import messages
from django.shortcuts import render , redirect
from django.db import transaction
from django.shortcuts import render , HttpResponseRedirect
from django.urls import reverse
from .forms import TaskRegistration
from .models import Task

from django.db.models.sql.subqueries import DeleteQuery


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
            messages.success(request, 'Updated Task Detail Successfully!!')
            fm.save()
            
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


#This function will add bulk data
def bulk_add(request):
    with transaction.atomic():
        for i in range(10):
            p = Task(title=f"Test Task{i}" , description = f"Lorem Ipsum is simply dummy text of the printing and typesetting industry.")
            p.save()
        return redirect('addandshow')


#This function will delete multiple tasks
def bulk_delete(qs):
    rows = Task.objects.filter(status = True)

    for r in rows:
        r.delete()
    return HttpResponseRedirect('/')

   
    
    