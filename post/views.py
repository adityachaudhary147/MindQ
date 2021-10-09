from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post,Comment
from .forms import NewCommentForm
# Create your views here.
from qna.models import Question
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def posts(request):
    if request.method == "POST":
        user = request.user
        description = request.POST.get("postDescription")
        url = request.POST.get("url")
        file = request.FILES['file']
        url = list(url.split(","))
        if url == ['']:
            url = ['none']
        form = Post(user=user,description=description,url=url,file=file)
        form.save()
        return redirect('posts')

    all_post = Post.objects.all().order_by('-created_on')
    context={'all_post':all_post}
    return render(request,'post/post.html',context)


@login_required(login_url='/login/')
def like_unlike_post(request):
    user = request.user.pk
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = User.objects.get(pk=user)

        if profile in post_obj.likes.all():
            post_obj.likes.remove(profile)
        else:
            post_obj.likes.add(profile)
            if profile in post_obj.dislikes.all():
                post_obj.dislikes.remove(profile)
        post_obj.save()

        

        data = {
            # 'likes': post_obj.likes.all().count()
        }

        return JsonResponse(data, safe=True)
    return redirect('posts:main-post-view')


@login_required(login_url='/login/')
def dislike_post(request):
    user = request.user.pk
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = User.objects.get(pk=user)

        if profile in post_obj.dislikes.all():
            post_obj.dislikes.remove(profile)
        else:
            post_obj.dislikes.add(profile)
            if profile in post_obj.likes.all():
                post_obj.likes.remove(profile)
        post_obj.save()

        
        data = {
            # 'dislikes': post_obj.dislikes.all().count()
        }

        return JsonResponse(data, safe=True)
    return redirect('posts:main-post-view')


@login_required(login_url='/login/')
def star_post(request):
    user = request.user.pk
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = User.objects.get(pk=user)

        if profile in post_obj.star.all():
            post_obj.star.remove(profile)
        else:
            post_obj.star.add(profile)
        post_obj.save()

        
        data = {
            # 'star': post_obj.star.all().count()
        }

        return JsonResponse(data,safe=True)
    return redirect('posts:main-post-view')


@login_required(login_url='/login/')
def postsingle(request,pk):
    v_post = Post.objects.get(id=int(pk))
    comment_form = NewCommentForm()
    if request.method == "POST":
        if request.method == 'POST':
            comment_form = NewCommentForm(request.POST)
            if comment_form.is_valid():
                user_comment = comment_form.save(commit=False)
                user_comment.post = v_post
                user_comment.user = request.user
                user_comment.save()
                return redirect('viewpost',pk)

    comment = Comment.objects.filter(post=v_post)
    count = comment.count()
    context = {'v_post': v_post, 'comments': comment,'comment_form':comment_form,'count':count}
    return render(request,'post/viewPost.html',context)
