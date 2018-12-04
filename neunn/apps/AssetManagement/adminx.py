# -*- coding:utf-8 -*-
__author__ = 'Lynn'
__data__ = '2018/10/30 13:17'

import xadmin

from .models import Resource1, Resource2, Resource3, Resource4, Resource5, Resource6


class Resource1Admin(object):
    list_display = ['name', 'ResourceType', 'Department', 'TenantName','Use', 'UserCategory', 'CPU', 'RAM', 'OS', 'Storage', 'PublicNetworkLineSelect', 'BandwidthType','Bandwidth', 'OpeningDate', 'ExpireDate','add_time']
    search_fields = ['name', 'ResourceType', 'Department', 'TenantName','Use', 'UserCategory', 'CPU', 'RAM', 'OS', 'Storage', 'PublicNetworkLineSelect', 'BandwidthType','Bandwidth', 'OpeningDate', 'ExpireDate']
    list_filter = ['name', 'ResourceType', 'Department', 'TenantName','Use', 'UserCategory', 'CPU', 'RAM', 'OS', 'Storage', 'PublicNetworkLineSelect', 'BandwidthType','Bandwidth', 'OpeningDate', 'ExpireDate']


class Resource2Admin(object):
    list_display = ['IntranetIP', 'FloatingIP', 'add_time']
    search_fields = ['IntranetIP', 'FloatingIP']
    list_filter = ['IntranetIP', 'FloatingIP']


class Resource3Admin(object):
    list_display = ['ExternalNetworkIP', 'IPMIP', 'add_time']
    search_fields = ['ExternalNetworkIP', 'IPMIP']
    list_filter = ['ExternalNetworkIP', 'IPMIP']


class Resource4Admin(object):
    list_display = ['ActualClosingTime' 'add_time']
    search_fields = ['ActualClosingTime']
    list_filter = ['ActualClosingTime']


class Resource5Admin(object):
    list_display = ['ResourceOpeningVerification', 'VirtualInstitution', 'add_time']
    search_fields = ['ResourceOpeningVerification', 'VirtualInstitution']
    list_filter = ['ResourceOpeningVerification', 'VirtualInstitution']


class Resource6Admin(object):
    list_display = ['CPUStorageUnitPrice', 'TotalCPUStorage', 'StorageUnitPrice', 'TotalStorage', 'BandwidthUnitPrice', 'TotalBandwidth', 'TotalPrice', 'add_time']
    search_fields = ['CPUStorageUnitPrice', 'TotalCPUStorage', 'StorageUnitPrice', 'TotalStorage', 'BandwidthUnitPrice', 'TotalBandwidth', 'TotalPrice']
    list_filter = ['CPUStorageUnitPrice', 'TotalCPUStorage', 'StorageUnitPrice',' TotalStorage', 'BandwidthUnitPrice', 'TotalBandwidth', 'TotalPrice']


xadmin.site.register(Resource1, Resource1Admin)
xadmin.site.register(Resource2, Resource2Admin)
xadmin.site.register(Resource3, Resource3Admin)
xadmin.site.register(Resource4, Resource4Admin)
xadmin.site.register(Resource5, Resource5Admin)
xadmin.site.register(Resource6, Resource6Admin)
