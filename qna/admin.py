from django.contrib import admin
from .models import Question,AnswerQ,Tag,Contact

# Register your models here.
admin.site.register(Question)
admin.site.register(AnswerQ)
admin.site.register(Tag)
admin.site.register(Contact)
