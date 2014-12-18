# -*- coding: utf-8 -*-
import chardet

#加密预处理，把id统一处理成16位
def deal_id(cnum):
	length = len(cnum)
	for i in range(0,16-length):
		cnum = cnum + "0"
	return cnum

#把数据库读出的记录(元组)与ckan的fields对应，形成一个1条记录的列表,输出为一条记录（字典）
def record_to_insert_to_ckan(ckan_fields,database_record):
	#统一编码成utf-8
	record = {}
	for i in range(1,len(ckan_fields)):
		ckan_fields[i]['id'] = ckan_fields[i]['id'].encode('utf-8')
		if isinstance(database_record[i-1],str):
			if chardet.detect(database_record[i-1])['encoding']!='utf-8':
				record[ckan_fields[i]['id']] = database_record[i-1].decode('gbk').encode('utf-8')
		elif isinstance(database_record[i-1],unicode):
			record[ckan_fields[i]['id']] = database_record[i-1].encode('utf-8')
		else:
			record[ckan_fields[i]['id']] = str(database_record[i-1])
	return record