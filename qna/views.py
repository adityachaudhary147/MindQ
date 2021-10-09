
from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from .models import Question,AnswerQ,Contact
from django.http import JsonResponse,HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib import messages

from post.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def redirectView(request):
    return redirect('questions')

def questions(request):
    context={}
    qs=Question.objects.all().order_by('-created_on')
    for i in range(len(qs)):
        qs[i].set_slug()
        print(qs[i].slug)
    voteup=[]
    for i in range(len(qs)):
        djshf=0
    context['qs']=qs
    return render(request,'index.html',context)

@login_required(login_url='/login/')
def questionsingle(request,pk):
    qs=Question.objects.all()
    for i in range(len(qs)):
        print(qs[i].slug)
    ques=Question.objects.filter(slug=pk)
    if len(ques)>0:
        ques=ques[0]
        ans=AnswerQ.objects.filter(question=ques).reverse()
        print(ans)
        for i in range(len(ans)):
            print(ans[i])
        context={}
        context['ans']=ans
        context['q']=ques
        return render(request,'qna/viewQuestion.html',context)
    else:
        return render(request,'notfound.html')
  
@login_required(login_url='/login/')
def createquestion(request):
    if request.method=='POST':
        print(request.user)
        title=request.POST.get('title')
        description=request.POST.get('description')
        url=request.POST.get('url')
        print(title,description,url)
        if (request.user.is_anonymous):
            return JsonResponse({'please login':"True"},safe=True)
        new1=Question(title=title,description=description,user=request.user,url=url)
        new1.save() 
        return JsonResponse({"safe":"safe"},safe=True)

@login_required(login_url='/login/')
def createanswer(request):
    if request.method=='POST':
        print(request.user)
        qid=request.POST.get('qid')
        urlt=request.POST.get('urlt')
        description=request.POST.get('description')
        print(qid)
        print(description)
        uu=Question.objects.filter(key=qid)
        if description==None:
            description="hello"
        newansw=AnswerQ(user=request.user,question=uu[0],description=description,url=urlt)
        newansw.save()
        # Some common views...
        return JsonResponse({"safe":"safe","urlt":urlt},safe=True)


@login_required(login_url='/login/')
def check(request):
    thread_id = int(request.GET.get('id'))
    thread = get_object_or_404(Question, key=thread_id)
    thisUserUpVote = thread.check_upvote(request.user)
    thisUserdownVote=thread.check_downvote(request.user)
    count=thread.count_votes()
    upvote=thisUserUpVote
    downvote=thisUserdownVote
    lis=[count,upvote,downvote]
    print(lis)
    return JsonResponse(lis,safe=False)

@login_required(login_url='/login/')
def vote(request):
   thread_id = int(request.POST.get('id'))
   vote_type = request.POST.get('vote')
   vote_action = request.POST.get('action')
   thread = get_object_or_404(Question, key=thread_id)
   if vote_action=='add' and vote_type=='down':
        thread.downvote.add(request.user)
        countvotes=thread.count_votes()
        return JsonResponse(countvotes,safe=False)
   if vote_action=='remove' and vote_type=='down':
        thread.downvote.remove(request.user)
        countvotes=thread.count_votes()
        return JsonResponse(countvotes,safe=False)
   if vote_action=='add' and vote_type=='up':
        thread.upvote.add(request.user)
        countvotes=thread.count_votes()
        return JsonResponse(countvotes,safe=False)
   if vote_action=='remove' and vote_type=='up':
       thread.upvote.remove(request.user)
       countvotes=thread.count_votes()
       return JsonResponse(countvotes,safe=False)


def about(request):
    return render(request,'qna/aboutus.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')
        form = Contact(name=name,email=email,phone=phone,query=query)
        print(name)
        form.save()
        return redirect('contactUs')
    return render(request,'qna/contact.html')

def peopleProfileView(request, id):
    print(id)
    user = User.objects.get(pk=int(id))
    print(user)
    posts = Post.objects.filter(user=user)
    qna = Question.objects.filter(user=user)
    return render(request,'user_profile/peopleProfile.html',context={'user':user,'posts':posts,'qna':qna})