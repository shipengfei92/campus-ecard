# -*- coding: utf-8 -*-
import sys
sys.path.append('..')
from moduals.ckan_methods import *

#ckan api information
ckan_host = '10.50.6.151'
ckan_api_key = 'c4ec2786-f178-468b-8122-8c24f4175c4d'

#write to ckan
print 'ckan_package_create:'
dataset_dict = {
	    'name': 'why_test',
	    'notes': 'A long description of my dataset',
}
ckan_package_create(ckan_host,ckan_api_key,dataset_dict)
print 'ckan_package_delete:'
dataset_dict = {
    'id': 'why_test',
}
ckan_package_delete(ckan_host,ckan_api_key,dataset_dict)
print 'ckan_resource_create:'
dataset_dict = {
    'package_id':'why_test',
    'url':'http://ckantest2.com',
    'name':'ckantest2',
    'format':'CSV',
    'upload':'/Users/wanghaiyang/workspace/ckantest.csv',
}
ckan_resource_create(ckan_host,ckan_api_key,dataset_dict)
print 'ckan_resource_update:'
dataset_dict = {
    'id':'d83068d9-914e-4862-a4d2-61a94baa21ad',
    'name':'ckantest3_modif',
    'format':'CSV',
     'upload':'/Users/wanghaiyang/workspace/ckantest.csv',
}
ckan_resource_update(ckan_host,ckan_api_key,dataset_dict)
print 'ckan_datastore_create:'
dataset_dict = {
	'resource_id': '8d28376a-70a3-4995-8278-8b25de32f3cf',
	'force': True,
	'fields': [{"id": "url_crc", "type": "text"},
			   {"id": "location", "type": "text"},
			   {"id": "province", "type": "text"},
			   {"id": "gender", "type": "text"},
			   {"id": "birthday", "type": "text"}
			  ],
	'primary_key':['url_crc'],
	'indexes':['url_crc','gender'],
}
ckan_datastore_create(ckan_host,ckan_api_key,dataset_dict)
dataset_dict = {
	'id': '8d28376a-70a3-4995-8278-8b25de32f3cf',
	'url': 'http://10.50.6.151/datastore/dump/' + '8d28376a-70a3-4995-8278-8b25de32f3cf',
}
ckan_resource_update(ckan_host,ckan_api_key,dataset_dict)
print 'ckan_datastore_upsert:'
data = [  {'url_crc':'86410937208069','location':'黑龙江 哈尔滨','province':'黑龙江','gender':'1','birthday':None},
		  {'url_crc':'86410937209070','location':'上海','province':'上海','gender':'1','birthday':None},
	   ]
dataset_dict = {
	"resource_id": '8d28376a-70a3-4995-8278-8b25de32f3cf',
	"force": True,
	"records": data,
	'method': 'upsert',
}
print dataset_dict
ckan_datastore_upsert(ckan_host,ckan_api_key,dataset_dict)
print 'ckan_datastore_delete'
dataset_dict = {
	"resource_id": '8d28376a-70a3-4995-8278-8b25de32f3cf',
	"force": True,
#	"filters":{'gender':'2',},
}
ckan_datastore_delete(ckan_host,ckan_api_key,dataset_dict)
print 'ckan_datastore_search:'
dataset_dict = {
	"resource_id": '8d28376a-70a3-4995-8278-8b25de32f3cf',
}
print ckan_datastore_search(ckan_host,ckan_api_key,dataset_dict)