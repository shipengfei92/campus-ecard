# -*- coding: utf-8 -*-
import cx_Oracle
import moduals.anonymous as m_anonym
import moduals.data_preprocessing as m_datapre

def read_oracle(db_user,db_passwd,db_host,db_port,db_sid):
	db_name = db_host + ":" + db_port + "/" + db_sid
	db = cx_Oracle.connect(db_user,db_passwd,db_name)
	cursor = db.cursor()
	sql = "select * from weibo where rownum<=20"
	cursor.execute(sql)
	lines = cursor.fetchall()
	for line in lines:
		for attr in line:
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