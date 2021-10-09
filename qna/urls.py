from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.redirectView,name='redirect'),
    # path('index.html',views.questions,name="index"),
    path('QnA',views.questions,name='questions'),
    path('question/<str:pk>',views.questionsingle,name="question"),
    path('createques',views.createquestion,name='create-question'),
    path('creatans',views.createanswer,name='create-answer'),
    path('vote',views.vote,name='vote'),
    path('check',views.check,name='check'),
    path('contact/',views.contact,name="contactUs"),
    path('about',views.about,name="about"),
    path('viewProfile/<int:id>/',views.peopleProfileView,name='viewProfile'),
]