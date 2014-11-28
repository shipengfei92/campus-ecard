# -*- coding: utf-8 -*-
import cx_Oracle
import hashlib
import sys

print sys.getdefaultencoding()

db_user = "wanghaiyang"
db_passwd = "wanghaiyang"
db_host = "202.120.32.27"
db_port = "1521"
db_sid = "ecard"
db_name = db_host + ":" + db_port + "/" + db_sid

db = cx_Oracle.connect(db_user,db_passwd,db_name)
cursor = db.cursor()
sql = "select * from weibo where rownum<=10"
cursor.execute(sql)
lines = cursor.fetchall()
for line in lines:
	for attr in line:
		if attr==line[0]:
			print attr,
			attr_anonym = hashlib.md5(attr).hexdigest()
			print attr_anonym,
		else:
			print attr,
	print
cursor.close()
db.close()