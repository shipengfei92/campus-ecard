# -*- coding: utf-8 -*-
import time
from moduals.database_methods import *
from conf.db_conf import *
from conf.ckan_conf import *

#database info
db_type = conf_db_type
db_user = conf_db_user
db_passwd = conf_db_passwd
db_host = conf_db_host
db_port = conf_db_port
db_sid = conf_db_sid
sql = conf_sql

#ckan info
ckan_host = conf_ckan_host
ckan_api_key = conf_ckan_api_key
ckan_resource_id = conf_ckan_resource_id
ckan_push_method = conf_ckan_push_method
ckan_datastore_rewrite = conf_ckan_datastore_rewrite


#delete old datastore
if ckan_datastore_rewrite:
	print ckan_resource_show(ckan_host,ckan_api_key,{'id': ckan_resource_id})['datastore_active']
	if ckan_resource_show(ckan_host,ckan_api_key,{'id': ckan_resource_id})['datastore_active']:
		print 'deleting old datastore'
		ckan_datastore_delete(ckan_host,ckan_api_key,{'resource_id': ckan_resource_id,"force": True})
	else:
		print 'datastore is null'

#update datastore's url
ckan_datastore_url = 'http://' + ckan_host + '/datastore/dump/' + ckan_resource_id
if ckan_datastore_url != ckan_resource_show(ckan_host,ckan_api_key,{'id': ckan_resource_id})['url']:
	ckan_resource_update(ckan_host,ckan_api_key,{'resource_id': ckan_resource_id,'url':ckan_datastore_url,"force": True})

#write to database
s_time = time.time()
if db_type == 'oracle':
	print 'creating datastore schema'
	ckan_schema_oracle(db_user,db_passwd,db_host,db_port,db_sid,sql,ckan_host,ckan_api_key,ckan_resource_id,ckan_push_method)
	print 'read from ' + db_type + ',writing to ckan,please wait……'
	read_oracle(db_user,db_passwd,db_host,db_port,db_sid,sql,ckan_host,ckan_api_key,ckan_resource_id,ckan_push_method)
elif db_type == 'mysql':
	print 'creating datastore schema'
	ckan_schema_mysql(db_user,db_passwd,db_host,db_port,db_sid,sql,ckan_host,ckan_api_key,ckan_resource_id,ckan_push_method)
	print 'read from ' + db_type + ',writing to ckan,please wait……'
	read_mysql(db_user,db_passwd,db_host,db_port,db_sid,sql,ckan_host,ckan_api_key,ckan_resource_id,ckan_push_method)
else:
	print 'other database is developing'
e_time = time.time()
print 'used time:',
print e_time-s_time


