# -*- coding: utf-8 -*-

#加密预处理，把id统一处理成16位
def deal_id(cnum):
	length = len(cnum)
	for i in range(0,16-length):
		cnum = cnum + "0"
	return cnum