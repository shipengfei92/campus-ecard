数据库—ckan 同步工具
===================================  
##介绍 

这是一个数据库同步工具，用户可以通过简单的配置，把多种数据库中的数据同步到ckan数据平台中。目前支持oracle/mysql两种数据库与ckan的同步，并具有数据加密与简单的数据预处理功能。
##环境要求
1.已安装好python2.7运行环境

2.安装python包
>cx_Oracle（oracle connector）
>mysql.connector（mysql connector）
>Crypto.Cipher import AES（数据加密）
>chardet（字符编码识别）

##使用方法 
需要两步，首先配置数据库的信息与ckan的信息，之后运行main.py文件即可把数据库的信息写入ckan的datastore中。
###配置
####1.配置数据库信息(conf/db_conf.py)
```python
conf_db_type =  '' #oracle/mysql
conf_db_user = ''
conf_db_passwd = ''
conf_db_host = ''
conf_db_port = ''
conf_db_sid = ''
conf_sql = ''
```
数据库连接信息、sql语句（支持单表或多表的数据同步）
####2.配置ckan信息(conf/ckan_conf.py)
```python
conf_ckan_host = ''
conf_ckan_api_key = ''
conf_ckan_resource_id = ''
conf_ckan_push_method = ''
conf_ckan_datastore_rewrite = True   #Bool var
```

###同步
```bash
python main.py
```
运行main.py函数即可实现数据库写入ckan
##未来工作
###1.简化代码
用petl工具简化代码量
###2.增加功能
支持对其他数据库同步的支持，例如SQL Server，sqlite等；
增加增量定时同步功能
###3.提高性能
进行测试找出瓶颈，对大量数据的插入，实现合理的分流功能，提高性能；
###4.友好界面
实现一个图形化界面，方面用户操作，直接在界面配置。