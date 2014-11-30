# -*- coding: utf-8 -*-
def deal_id(cnum):
	length = len(cnum)
	for i in range(0,16-length):
		cnum = cnum + "0"
	return cnum