# -*- coding: utf-8 -*-
import requests

#ckan api information

#根据fields，添加记录
import chardet
import urllib

rawdata = urllib.urlopen('http://www.google.cn/').read().decode('utf-8').encode('gbk')
rawdata = 'ha'.encode('gbk')
print chardet.detect(rawdata)