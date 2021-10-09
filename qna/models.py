from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django_mysql.models import ListCharField,ListTextField
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
from django.utils.text import slugify


class Question(models.Model):
    key = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="QUser")
    title = models.CharField(max_length=300,blank=False)
    description = models.TextField(blank=True)
    url = ListTextField(base_field=CharField(max_length=300,blank=True),size=10,blank=True,default='')
    tags = models.ManyToManyField("Tag",related_name="QTag")
    created_on = models.DateTimeField(auto_now_add=True)
    upvote = models.ManyToManyField(User,related_name="QUpVote")
    downvote = models.ManyToManyField(User,related_name="QDownVote")
    slug = models.SlugField(max_length=300,default="set-some-slug-bro")
    
    def set_slug(self):
        self.slug=slugify(self.title)
        self.save()
        return
    def __str__(self):
        return self.title
    def count_upvotes(self):
        return self.upvote.count()
    def check_upvote(self,user23):
        return self.upvote.filter(id=user23.id).exists()
    def count_downvotes(self):
        return self.downvote.count()
    def check_downvote(self,user23):
        return self.downvote.filter(id=user23.id).exists()
    def count_votes(self):
        return self.count_upvotes()-self.count_downvotes()


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)
    def __str__(self):
        return self.tag_name

class AnswerQ(MPTTModel):
    key = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="QAnswere")
    parent = TreeForeignKey('self', on_delete=models.CASCADE,null=True,blank=True, related_name='children')
    url = ListTextField(base_field=CharField(max_length=300,blank=True),size=10,blank=True,null=True,default="")
    description = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['created_on']

    def __str__(self):
        return self.description


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    query = models.TextField(blank=True)

    def __str__(self):
        return self.name
