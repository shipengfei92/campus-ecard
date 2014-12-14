# -*- coding: utf-8 -*-
from moduals.read_modual import *
from moduals.write_modual import *

#read form database
print 'Oracle:'
#read_oracle(oracle_db_user,oracle_db_passwd,oracle_db_host,oracle_db_port,oracle_db_sid)
print 'MySQL:'
read_mysql(mysql_db_user,mysql_db_passwd,mysql_db_host,mysql_db_port,mysql_db_sid)

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
    'name':'ckantest',
    'format':'CSV',
    'upload':'/Users/wanghaiyang/workspace/ckantest.csv',
}
ckan_resource_create(ckan_host,ckan_api_key,dataset_dict)

