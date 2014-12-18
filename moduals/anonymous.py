# /usr/bin/python
# -*- coding:utf-8 -*-

from Crypto.Cipher import AES

pass_key = "wedpspkfij198@*9oksplakihsnxij%#"

def aes_encrypt(key,message):
	obj = AES.new(key, AES.MODE_ECB)
	ciphertext = obj.encrypt(message)
	ciphertext = ciphertext.encode("hex")
	return ciphertext

def aes_decrypt(key,ciphertext):
	obj = AES.new(key, AES.MODE_ECB)
	message = obj.decrypt(ciphertext.decode("hex"))
	return message