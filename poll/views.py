from django.shortcuts import render
from poll.models import *
from django.http import Http404,HttpResponse

# Create your views here.

def index(request):
    questions=Question.objects.all()
    context={}
    context['title']='polls'
    context['questions']=questions
    return render(request,'polls/index.html',context)
def details(request,id=id):
    context={}
    try:
        questions=Question.objects.get(id=id)
    except:
        raise Http404
    # context['title']='polls'
    context['questions']=questions
    return render(request,'polls/details.html',context)
def poll(request,id=id):
    context={}
    if request.method=="GET":
        try:
            questions=Question.objects.get(id=id)
        except:
            raise Http404
        context['questions']=questions
        return render(request,"Polls/poll.html",context)
    if request.method=="POST":
        user_id=1
        print(request.POST)
        data=request.POST
        ret=Answer.objects.create(user_id=user_id,choice_id=data["choice"])
        if ret:
            return HttpResponse("Your vote is succesful")
        else:
            return HttpResponse("Your vote not is succesful")
