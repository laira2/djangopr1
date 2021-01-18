import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) #질문내용 CharField는 형식 지정
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date>= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE) 
    #선택지에 해당하는 질문 Foreignkey-> 외래키 Question의 data모델을 참조 = choice의 question은 Question을 가리킴
    # CASCADE Question이 삭제되면 Choice의 question도 삭제    
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 
    #하나의 Question에 여러 답을 받음 = 1대 다
    def __str__(self):
        return self.choice_text
    