# -*- coding: utf-8 -*-

import moduals.read_modual as m_read

db_user = "wanghaiyang"
db_passwd = "wanghaiyang"
db_host = "202.120.32.27"
db_port = "1521"
db_sid = "ecard"

print "Oracle:"
m_read.read_oracle(db_user,db_passwd,db_host,db_port,db_sid)
print "MySQL:"
m_read.read_mysql('wanghaiyang','wanghaiyang','10.50.15.191','3306','omnilab_bd')
