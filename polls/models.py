import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date pushlished')

datetime.timedelta(days=1)

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class playground(models.Model):
    Pid = models.AutoField(max_length = 4, primary_key = True)
    Pname = models.CharField(max_length = 20, blank = False, unique = True)
    Pinfomation = models.CharField(max_length = 400,  blank = False)
    Popentime = models.DateTimeField(db_column = 'Popentime', blank = False)
    Ptel = models.IntegerField(max_length = 8, blank = False)
    Padderss = models.CharField(max_length = 100, blank = False)

class userBaseInfo(models.Model):
    Uid = models.AutoField(max_length = 4, primary_key = True)
    Uname = models.CharField(max_length = 20, blank = False)
    Utel = models.IntegerField(max_length = 8, blank = False)
    Usign = models.CharField(max_length = 200, blank = False)
    Usex = models.CharField(max_length = 2, blank = False)
    Ubirthdate = models.DateField(blank = False, default = datetime.datetime.now().date())

class userDynamicInfo(models.Model):
    DIid = models.IntegerField(max_length = 11)
    Uaddress = models.IntegerField()


class project(models.Model):
    proid = models.AutoField(max_length = 8,primary_key = True)
    proname = models.CharField(max_length = 30,blank = False)
    prodesc = models.CharField(max_length = 400,blank = False)
    pmark = models.FloatField(blank = False)
    proplay = models.ForeignKey(playground)

class ticket(models.Model):
    Tid = models.AutoField(max_length = 8, primary_key = True)
    Ttype = models.CharField(max_length = 20, blank = False, default = '空')
    Tprice = models.FloatField(blank = False, default = 0.00)
    Tdatetime = models.DateTimeField(blank = False)
    Tproject = models.ForeignKey(project)
    TplaygroundId_id = models.ForeignKey(playground)

class entertainment(models.Model):
    Ename = models.CharField(max_length = 20, blank = False)
    Eaddress = models.CharField(max_length = 100, blank = False)
    Eopentime = models.DateTimeField(blank = False)
    Emax_num = models.IntegerField(max_length = 4, blank = False, default = 0)
    Eonce_time = models.CharField(max_length = 20, blank = False)

class userticket(models.Model):
    Uid = models.IntegerField(max_length = 4,blank = False)
    Uticket = models.ForeignKey(ticket)
    Uticketstatus = models.IntegerField(max_length = 4,blank = False ,default = 0)

class Comment(models.Model):
    Cid = models.AutoField(max_length = 8, primary_key = True)
    Cuid = models.IntegerField(max_length = 11, db_column = 'Cuid')
    Ctime = models.DateTimeField(blank = False, default = datetime.datetime.now())
    Clight = models.IntegerField(max_length = 4, blank = False, default = 0)
    Cfloor = models.IntegerField(max_length = 4, blank = False, default = 0)
    Ccontent = models.CharField(max_length = 400, blank = False)
    Cproject = models.ForeignKey(project)

    # Create your models here.
