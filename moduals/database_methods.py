# -*- coding: utf-8 -*-
import cx_Oracle
import mysql.connector

from moduals.anonymous import *
from moduals.data_preprocessing import *
from moduals.ckan_methods import *

#read from database
def read_oracle(db_user,db_passwd,db_host,db_port,db_sid,oracle_sql,ckan_host,ckan_api_key,ckan_datastore,push_method):
	#get the datastore's ID to insert
	dataset_dict = {
		"resource_id": ckan_datastore,
	}
	result = ckan_datastore_get_fields(ckan_host,ckan_api_key,dataset_dict)
	#read from oracle database and insert them to ckan datastore
	db_name = db_host + ":" + db_port + "/" + db_sid
	db = cx_Oracle.connect(db_user,db_passwd,db_name)
	cursor = db.cursor()
	cursor.execute(oracle_sql)
	print cursor.description
	data = []
	for line in cursor:
		data.append(record_to_insert_to_ckan(result,line))
	dataset_dict = {
		"resource_id": ckan_datastore,
		"force": True,
		"records": data,
		'method': push_method,
	}
	ckan_datastore_upsert(ckan_host,ckan_api_key,dataset_dict)
	cursor.close()
	db.close()

def read_mysql(db_user,db_passwd,db_host,db_port,db_sid,mysql_sql,ckan_host,ckan_api_key,ckan_datastore,push_method):
	#get the datastore's ID to insert
	dataset_dict = {
		"resource_id": ckan_datastore,
	}
	result = ckan_datastore_get_fields(ckan_host,ckan_api_key,dataset_dict)
	#read from mysql database and insert them to ckan datastore
	conn = mysql.connector.connect(user=db_user,password=db_passwd,host=db_host,port=db_port,database=db_sid)
	cursor = conn.cursor()
	cursor.execute(mysql_sql)
	print cursor.description
	data = []
	for line in cursor:
		data.append(record_to_insert_to_ckan(result,line))
	dataset_dict = {
			"resource_id": ckan_datastore,
			"force": True,
			"records": data,
			'method': push_method,
	}
	ckan_datastore_upsert(ckan_host,ckan_api_key,dataset_dict)
	cursor.close()
	conn.close()