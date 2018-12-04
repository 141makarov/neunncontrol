# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.


class Resource1(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"申请人")
    ResourceType = models.CharField(max_length=50, verbose_name=u"资源类型")
    Department = models.CharField(max_length=50, verbose_name=u"部门")
    TenantName = models.CharField(max_length=50, verbose_name=u"租户名")
    Use = models.CharField(max_length=100, verbose_name=u"用途")
    UserCategory = models.CharField(max_length=50, default=u"内部用户", verbose_name=u"用户类型")
    CPU = models.IntegerField(default=32, verbose_name=u"CPU/核")
    RAM = models.IntegerField(default=128, verbose_name=u"内存(G)")
    OS = models.CharField(max_length=50, verbose_name=u"操作系统")
    Storage = models.IntegerField(default=0, verbose_name=u"存储(G)")
    PublicNetworkLineSelect = models.CharField(max_length=50, verbose_name=u"公用线路选择")
    BandwidthType = models.CharField(max_length=50, verbose_name=u"带宽类型")
    Bandwidth = models.IntegerField(default=0, verbose_name=u"带宽(M)")
    OpeningDate = models.DateTimeField(default=datetime.now, verbose_name=u"开通时间")
    ExpireDate = models.DateTimeField(default=datetime.now, verbose_name=u"到期时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "资源一"
        verbose_name_plural = verbose_name


class Resource2(models.Model):
    IntranetIP = models.CharField(max_length=50, verbose_name=u"内网IP")
    FloatingIP = models.CharField(max_length=50, verbose_name=u"浮动IP")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "资源2"
        verbose_name_plural = verbose_name


class Resource3(models.Model):
    ExternalNetworkIP = models.CharField(max_length=50, verbose_name=u"外网IP")
    IPMIP = models.CharField(max_length=50, verbose_name=u"IPM的IP")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "资源3"
        verbose_name_plural = verbose_name


class Resource4(models.Model):
    ActualClosingTime = models.DateTimeField(default=datetime.now, verbose_name=u"实际关闭时间")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "资源4"
        verbose_name_plural = verbose_name


class Resource5(models.Model):
    ResourceOpeningVerification = models.BooleanField(default=False, verbose_name=u"资源开通核实")
    VirtualInstitution = models.BooleanField(default=False, verbose_name=u"虚机关电")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "资源5"
        verbose_name_plural = verbose_name


class Resource6(models.Model):
    CPUStorageUnitPrice = models.IntegerField(default=0, verbose_name=u"CPU与内存组合单价")
    TotalCPUStorage = models.IntegerField(default=0, verbose_name=u"总价")
    StorageUnitPrice = models.IntegerField(default=0, verbose_name=u"存储单价")
    TotalStorage = models.IntegerField(default=0, verbose_name=u"存储总价")
    BandwidthUnitPrice = models.IntegerField(default=0, verbose_name=u"带宽单价")
    TotalBandwidth = models.IntegerField(default=0, verbose_name=u"带宽总价")
    TotalPrice = models.IntegerField(default=0, verbose_name=u"总价")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = "资源6"
        verbose_name_plural = verbose_name

