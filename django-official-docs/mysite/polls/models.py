from django.db import models
from django.utils import timezone
import datetime


# *** notes by crz at 2021-09-01 08:42 *** :
# 针对数据对象的一些操作命令
# Question.objects.all() .filter(id=1) .filter(question_text__startswith='what') .get(pub_date__year=current_year) .get(pk=1)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(verbose_name='date published', auto_now_add=True)

    # *** notes by crz at 2021-09-01 08:23 *** : shows when calling Question.objects.all()
    # It’s important to add __str__() methods to your models,
    # not only for your own convenience when dealing with the interactive prompt,
    # but also because objects’ representations are used throughout Django’s automatically-generated admin.
    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# *** notes by crz at 2021-09-01 08:50 *** :
# q = Question.objects.get(pk=1)
# q.choice_set.all()
# q.choice_set.create(choice_text='Not much', votes=0)
# q.choice_set.create(choice_text='The sky', votes=0) 
# c = q.choice_set.create(choice_text='Just hacking again', votes=0)
# c.question
# q.choice_set.all()
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text


