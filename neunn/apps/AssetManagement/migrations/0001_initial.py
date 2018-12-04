# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-10-30 11:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u7533\u8bf7\u4eba')),
                ('Department', models.CharField(max_length=50, verbose_name='\u90e8\u95e8')),
                ('TenantName', models.CharField(max_length=50, verbose_name='\u79df\u6237\u540d')),
                ('Use', models.CharField(max_length=100, verbose_name='\u7528\u9014')),
                ('ResourceType', models.CharField(max_length=50, verbose_name='\u7528\u6237\u7c7b\u578b')),
                ('CPU', models.IntegerField(default=32, verbose_name='CPU/\u6838')),
                ('RAM', models.IntegerField(default=128, verbose_name='\u5185\u5b58(G)')),
                ('OS', models.CharField(max_length=50, verbose_name='\u64cd\u4f5c\u7cfb\u7edf')),
                ('Storage', models.IntegerField(default=0, verbose_name='\u5b58\u50a8(G)')),
                ('PublicNetworkLineSelect', models.CharField(max_length=50, verbose_name='\u516c\u7528\u7ebf\u8def\u9009\u62e9')),
                ('BandwidthType', models.CharField(max_length=50, verbose_name='\u5e26\u5bbd\u7c7b\u578b')),
                ('Bandwidth', models.IntegerField(default=0, verbose_name='\u5e26\u5bbd(M)')),
                ('OpeningDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u5f00\u901a\u65f6\u95f4')),
                ('ExpireDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u5230\u671f\u65f6\u95f4')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8d44\u6e90\u4e00',
                'verbose_name_plural': '\u8d44\u6e90\u4e00',
            },
        ),
        migrations.CreateModel(
            name='Resource2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IntranetIP', models.CharField(max_length=50, verbose_name='\u5185\u7f51IP')),
                ('FloatingIP', models.CharField(max_length=50, verbose_name='\u6d6e\u52a8IP')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8d44\u6e902',
                'verbose_name_plural': '\u8d44\u6e902',
            },
        ),
        migrations.CreateModel(
            name='Resource3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExternalNetworkIP', models.CharField(max_length=50, verbose_name='\u5916\u7f51IP')),
                ('IPMIP', models.CharField(max_length=50, verbose_name='IPM\u7684IP')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8d44\u6e903',
                'verbose_name_plural': '\u8d44\u6e903',
            },
        ),
        migrations.CreateModel(
            name='Resource4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActualClosingTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u5b9e\u9645\u5173\u95ed\u65f6\u95f4')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8d44\u6e904',
                'verbose_name_plural': '\u8d44\u6e904',
            },
        ),
        migrations.CreateModel(
            name='Resource5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResourceOpeningVerification', models.BooleanField(default=False, verbose_name='\u8d44\u6e90\u5f00\u901a\u6838\u5b9e')),
                ('VirtualInstitution', models.BooleanField(default=False, verbose_name='\u865a\u673a\u5173\u7535')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8d44\u6e905',
                'verbose_name_plural': '\u8d44\u6e905',
            },
        ),
        migrations.CreateModel(
            name='Resource6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPUStorageUnitPrice', models.IntegerField(default=0, verbose_name='CPU\u4e0e\u5185\u5b58\u7ec4\u5408\u5355\u4ef7')),
                ('TotalCPUStorage', models.IntegerField(default=0, verbose_name='\u603b\u4ef7')),
                ('StorageUnitPrice', models.IntegerField(default=0, verbose_name='\u5b58\u50a8\u5355\u4ef7')),
                ('TotalStorage', models.IntegerField(default=0, verbose_name='\u5b58\u50a8\u603b\u4ef7')),
                ('BandwidthUnitPrice', models.IntegerField(default=0, verbose_name='\u5e26\u5bbd\u5355\u4ef7')),
                ('TotalBandwidth', models.IntegerField(default=0, verbose_name='\u5e26\u5bbd\u603b\u4ef7')),
                ('TotalPrice', models.IntegerField(default=0, verbose_name='\u603b\u4ef7')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u8d44\u6e906',
                'verbose_name_plural': '\u8d44\u6e906',
            },
        ),
    ]
