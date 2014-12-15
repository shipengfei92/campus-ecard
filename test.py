# -*- coding: utf-8 -*-
import requests

#ckan api information
dataset_dict = {
	    'name': 'why_test',
	    'notes': 'A long description of my dataset',
}

print dataset_dict.has_key('name')
print dataset_dict.has_key('name1')

