# -*- coding: utf-8 -*-
from moduals.read_modual import *
from moduals.write_modual import *

#oracle connection information
oracle_db_user = 'wanghaiyang'
oracle_db_passwd = 'wanghaiyang'
oracle_db_host = '202.120.32.27'
oracle_db_port = '1521'
oracle_db_sid = 'ecard'
oracle_sql = 'select * from weibo where rownum<=20'

#mysql connection information
mysql_db_user = 'wanghaiyang'
mysql_db_passwd = 'wanghaiyang'
mysql_db_host = '10.50.15.191'
mysql_db_port = '3306'
mysql_db_sid = 'omnilab_bd'
mysql_sql = 'select url_crc,location,province,gender,birthday from w_user_info_distinct limit 20'
# mysql_sql = 'desc w_user_info_distinct'

#ckan api information
ckan_host = '10.50.6.151'
ckan_api_key = 'c4ec2786-f178-468b-8122-8c24f4175c4d'

#read form database
print 'Oracle:'
#read_oracle(oracle_db_user,oracle_db_passwd,oracle_db_host,oracle_db_port,oracle_db_sid,oracle_sql)
print 'MySQL:'
read_mysql(mysql_db_user,mysql_db_passwd,mysql_db_host,mysql_db_port,mysql_db_sid,mysql_sql)

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
print 'ckan_rsource_create:'
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
			   {"id": "gender", "type": "int"},
			   {"id": "birthday", "type": "int"}
			  ],
}
ckan_datastore_create(ckan_host,ckan_api_key,dataset_dict)
dataset_dict = {
	'id': '8d28376a-70a3-4995-8278-8b25de32f3cf',
	'url': 'http://10.50.6.151/datastore/dump/' + '8d28376a-70a3-4995-8278-8b25de32f3cf',
}
ckan_resource_update(ckan_host,ckan_api_key,dataset_dict)
print 'ckan_datastore_upsert:'
data = [{'url_crc':'86410937208069','location':'黑龙江 哈尔滨','province':'黑龙江','gender':'2','birthday':None}]
dataset_dict = {
	"resource_id": '8d28376a-70a3-4995-8278-8b25de32f3cf',
	"force": True,
	"records": data,
	'method': 'insert',
}
ckan_datastore_upsert(ckan_host,ckan_api_key,dataset_dict)
