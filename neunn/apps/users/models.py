# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default=u"")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(("male", u"男"), ("female", u"女")), default="female")
    address = models.CharField(max_length=100, default=u"")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%X", default=u"image/default.png")

    class Meta:
        verbose_name = "用户列表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.CharField(max_length=20, choices=(("register",u"注册"), ("forget", u"忘记密码"), ("found", u"找回密码")))
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


