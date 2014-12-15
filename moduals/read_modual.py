# -*- coding: utf-8 -*-
import cx_Oracle
import mysql.connector

import moduals.anonymous as m_anonym
import moduals.data_preprocessing as m_datapre

def read_oracle(db_user,db_passwd,db_host,db_port,db_sid,oracle_sql):
	db_name = db_host + ":" + db_port + "/" + db_sid
	db = cx_Oracle.connect(db_user,db_passwd,db_name)
	cursor = db.cursor()
	cursor.execute(oracle_sql)
	print cursor.description
	for line in cursor:
		for attr in line:
			#do some operations here
			if attr==line[0]:
				print attr,
				attr = m_datapre.deal_id(attr)
				print attr,
				attr_anonym = m_anonym.aes_encrypt(m_anonym.key,attr)
				print attr_anonym,
				print m_anonym.aes_decrypt(m_anonym.key,attr_anonym),
			else:
				if attr!=None:
					attr = attr.decode("gbk")
				print attr,
		print
	cursor.close()
	db.close()

def read_mysql(db_user,db_passwd,db_host,db_port,db_sid,mysql_sql):
	conn = mysql.connector.connect(user=db_user,password=db_passwd,host=db_host,port=db_port,database=db_sid)
	cursor = conn.cursor()
	cursor.execute(mysql_sql)
	print cursor.description
	print cursor.column_names
	for line in cursor:
		for attr in line:
			print attr,
		print
	cursor.close()
	conn.close()