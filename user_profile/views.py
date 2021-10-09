from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from django.http import JsonResponse
from post.models import Post
from qna.models import Question

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def profilePage(request):
    #a = request.user.socialaccount_set.filter(provider='google')[0].extra_data['picture']
    #print(a)
    user = request.user
    all_post = Post.objects.filter(user=user)
    qs = Question.objects.filter(user=user)
    fav_post = Post.objects.filter(star=user)
    user_profile = Profile.objects.get(user=user)
    if request.method == "POST":
        job = request.POST.get('job')
        bio = request.POST.get('bio')
        user_profile.job = job
        user_profile.bio = bio
        user_profile.save()
        return redirect('profile')


    context={'all_post':all_post,'qs':qs,'fav_post':fav_post,'follower':user_profile}
    return render(request,'user_profile/profile.html',context)

@login_required(login_url='/login/')
def peopleYouMayKnow(request):
    profiles = Profile.objects.all().order_by('-account_created')
    context = {'profiles':profiles}
    return render(request,'user_profile/peopleYouMayKnow.html',context)

@login_required(login_url='/login/')
def followView(request):
    user = request.user.pk
    if request.method == 'POST':
        profile_id = request.POST.get('profile_id')
        print(profile_id)
        profile_obj = Profile.objects.get(key=profile_id)
        profile = User.objects.get(pk=user)

        profile_obj_2 = Profile.objects.get(key=user)
        profile_2 = User.objects.get(pk=int(profile_id))

        if profile_2 in profile_obj_2.following.all():
            profile_obj_2.following.remove(profile_2)
        else:
            profile_obj_2.following.add(profile_2)
        profile_obj_2.save()


        if profile in profile_obj.followers.all():
            profile_obj.followers.remove(profile)
        else:
            profile_obj.followers.add(profile)
        profile_obj.save()
        

        data = {
            'likes': profile_obj.followers.all().count()
        }

        return JsonResponse(data, safe=True)
    return redirect('user_profile:profile')


@login_required(login_url='/login/')
def profileImageUpdate(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    if request.method == "POST":
        profile_image = request.FILES['profile_image']
        user_profile.profile_image = profile_image
        user_profile.save()
        return redirect('profile')


