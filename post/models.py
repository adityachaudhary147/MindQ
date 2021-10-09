from django.db import models
from django_mysql.models import ListTextField
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey

class Post(models.Model):

    visibility = [
        ('Show','Show'),
        ('Hide','Hide')
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000,blank=True,null=True)
    url = ListTextField(base_field=models.CharField(max_length=300,blank=True),size=10,default='',blank=True)
    file = models.FileField(upload_to='posts/',blank=True)
    likes = models.ManyToManyField(User, related_name="P_like")
    dislikes = models.ManyToManyField(User, related_name="P_dislike")
    star = models.ManyToManyField(User, related_name="s_post")
    created_on = models.DateTimeField(auto_now_add=True)
    visible = models.CharField(max_length=10,choices=visibility,default='Show')
    
    def __str__(self):
        return self.description

    def num_likes(self):
        return self.likes.all().count()

    def num_dislikes(self):
        return self.dislikes.all().count()

    


class Comment(MPTTModel):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    content = models.TextField(blank=True)
    url = ListTextField(base_field=models.CharField(max_length=300),size=10,blank=True,null=True,default="")
    created_on = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['created_on']

    def __str__(self):
        return self.content

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
