from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from employee.forms import UserForm

def user_login(request):
    context={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('user_success'))
        else:
            context["error"]="provide a valid credentials"
            return render(request,"auth/login.html",context)
    else:
        return render(request,"auth/login.html",context)

def success(request):
    context={}
    context['user']=request.user
    return render(request,"auth/success.html",context)

def user_logout(request):
    if request.method=="POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))

# Create your views here.
def employee_list(request):
    context={}
    context['user']=User.objects.all()
    context['title']='Employees'
    return render(request,'employee/index.html',context)

def employee_details(request,id=id):
    context={}
    context['user']=get_object_or_404(User,id=id)
    return render(request,'employee/details.html',context)

def employee_edit(request,id=id):
    user=get_object_or_404(User,id=id)
    if request.method=='POST':
        user_form=UserForm(request.POST,instance=user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request,'employee/add.html',{"user_form":user_form})
    else:
        user_form=UserForm(instance=user)
        return render(request,'employee/add.html',{"user_form":user_form})


def employee_add(request):
    if request.method=='POST':
        user_form=UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            return render(request,'employee/add.html',{"user_form":user_form})
    else:
        user_form=UserForm()
        return render(request,'employee/add.html',{"user_form":user_form})
def employee_delete(request, id=None):
    user = get_object_or_404(User, id=id)
    print(user)
    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('employee_list'))
    else:
        context = {}
        context['user'] = user
        return render(request, 'employee/delete.html', context)
