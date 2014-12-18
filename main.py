# -*- coding: utf-8 -*-
import time
from moduals.database_methods import *


#oracle connection information
oracle_db_user = 'wanghaiyang'
oracle_db_passwd = 'wanghaiyang'
oracle_db_host = '202.120.32.27'
oracle_db_port = '1521'
oracle_db_sid = 'ecard'
oracle_sql = 'select url_crc,location,province,gender,birthday from weibo where rownum<=100'

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
resource_id = '8d28376a-70a3-4995-8278-8b25de32f3cf'
push_method = 'upsert'

#read form database and write to ckan
print 'Oracle:'
s_time = time.time()
read_oracle(oracle_db_user,oracle_db_passwd,oracle_db_host,oracle_db_port,oracle_db_sid,oracle_sql,ckan_host,ckan_api_key,resource_id,push_method)
e_time = time.time()
print '所用时间:',
print e_time-s_time
print 'MySQL:'
s_time = time.time()
read_mysql(mysql_db_user,mysql_db_passwd,mysql_db_host,mysql_db_port,mysql_db_sid,mysql_sql,ckan_host,ckan_api_key,resource_id,push_method)
e_time = time.time()
print '所用时间:',
print e_time-s_time


