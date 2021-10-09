from django.urls import path

from . import views

urlpatterns = [
    path('',views.profilePage,name="profile"),
    path('people_you_may_know/',views.peopleYouMayKnow,name="peopleYouMayKnow"),
    path("follow/",views.followView,name="follow-view"),
    path('profileUpdate',views.profileImageUpdate,name='profileUpdate'),

]