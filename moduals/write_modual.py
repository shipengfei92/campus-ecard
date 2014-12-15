# -*- coding: utf-8 -*-
import urllib2
import urllib
import json
import pprint
import requests

#write to ckan
def ckan_common(func_type,host,api_key,dataset_dict):
	request = urllib2.Request(
	    'http://' + host + '/api/3/action/' + func_type)
	request.add_header('Authorization', api_key)

	response = urllib2.urlopen(request, dataset_dict)
	assert response.code == 200

	response_dict = json.loads(response.read())
	assert response_dict['success'] is True

	# package_create returns the created package as its result.
	response_result = response_dict['result']
	pprint.pprint(response_result)

def ckan_package_create(host,api_key,dataset_dict):
	data_string = urllib.quote(json.dumps(dataset_dict))
	ckan_common('package_create',host,api_key,data_string)


def ckan_package_delete(host,api_key,dataset_dict):
	data_string = urllib.quote(json.dumps(dataset_dict))
	ckan_common('package_delete',host,api_key,data_string)

def ckan_resource_create(host,api_key,dataset_dict):
	if dataset_dict.has_key('upload'):
		url = 'http://' + host + '/api/3/action/resource_create'
		file_valua = dataset_dict['upload']
		del dataset_dict['upload']
		requests.post(url,data=dataset_dict,headers={'Authorization':api_key},files=[('upload', file(file_valua))])
	else:
		data_string = urllib.quote(json.dumps(dataset_dict))
		ckan_common('resource_create',host,api_key,data_string)

def ckan_resource_update(host,api_key,dataset_dict):
	if dataset_dict.has_key('upload'):
		url = 'http://' + host + '/api/3/action/resource_update'
		file_valua = dataset_dict['upload']
		del dataset_dict['upload']
		requests.post(url,data=dataset_dict,headers={'Authorization':api_key},files=[('upload', file(file_valua))])
	else:
		data_string = urllib.quote(json.dumps(dataset_dict))
		ckan_common('resource_update',host,api_key,data_string)

def ckan_datastore_create(host,api_key,dataset_dict):
	data_string = urllib.quote(json.dumps(dataset_dict))
	ckan_common('datastore_create',host,api_key,data_string)

def ckan_datastore_upsert(host,api_key,dataset_dict):
	data_string = urllib.quote(json.dumps(dataset_dict))
	ckan_common('datastore_upsert',host,api_key,data_string)

	

	