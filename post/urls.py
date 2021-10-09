from django.urls import path

from . import views

urlpatterns = [
    path('',views.posts,name='posts'),
    path('viewpost/<int:pk>/',views.postsingle,name="viewpost"),
    path('liked/', views.like_unlike_post, name='like-post-view'),
    path('disliked/', views.dislike_post, name='dislike-post-view'),
    path('star/', views.star_post, name='star-post-view'),
]