# -*- coding: utf-8 -*-
import cx_Oracle
import mysql.connector

from moduals.anonymous import *
from moduals.data_preprocessing import *
from moduals.ckan_methods import *

#oracle
def ckan_schema_oracle(db_user,db_passwd,db_host,db_port,db_sid,oracle_sql,ckan_host,ckan_api_key,ckan_datastore,push_method):
	#get oracle schema information
	db_name = db_host + ":" + db_port + "/" + db_sid
	db = cx_Oracle.connect(db_user,db_passwd,db_name)
	cursor = db.cursor()
	cursor.execute(oracle_sql)
	oracle_desc = cursor.description
	cursor.close()
	db.close()
	#write oracle schema to ckan
	fields = schema_insert_to_ckan(oracle_desc)
	dataset_dict = {
		"resource_id": ckan_datastore,
		"force": True,
		"fields": fields,
		'primary_key':fields[0]['id'],
	}
	ckan_datastore_create(ckan_host,ckan_api_key,dataset_dict)

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

#mysql
def ckan_schema_mysql(db_user,db_passwd,db_host,db_port,db_sid,mysql_sql,ckan_host,ckan_api_key,ckan_datastore,push_method):
	#get mysql schema information
	mysql_sql = mysql_sql.split(' limit ')[0] + ' limit 1'
	conn = mysql.connector.connect(user=db_user,password=db_passwd,host=db_host,port=db_port,database=db_sid)
	cursor = conn.cursor(buffered=True)
	cursor.execute(mysql_sql)
	mysql_desc = cursor.description
	cursor.close()
	conn.close()
	#write mysql schema to ckan
	fields = schema_insert_to_ckan(mysql_desc)
	dataset_dict = {
		"resource_id": ckan_datastore,
		"force": True,
		"fields": fields,
		'primary_key':fields[0]['id'],
	}
	ckan_datastore_create(ckan_host,ckan_api_key,dataset_dict)

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