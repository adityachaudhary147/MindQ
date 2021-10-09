from django import forms
from django.contrib.auth.models import User
from .models import Comment, Post
from mptt.forms import TreeNodeChoiceField

class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('parent','content')

        widgets = {
            'content': forms.Textarea(attrs={'class': 'newComment','placeholder':'Add a new comment'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(NewCommentForm, self).save(*args, **kwargs)


