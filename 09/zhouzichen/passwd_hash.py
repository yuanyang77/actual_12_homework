#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,hashlib


def encrypt_password(password, salt=None):
	if salt is None:
		salt =os.urandom(8)
	salt = 'zhoulouz'
	#windows编码已吐血，迫不得已
	assert 8 == len(salt)
	assert isinstance(salt,str)

	if isinstance(password,unicode):
			password = password.encode('utf-8')

	assert isinstance(password,str)

	result = password
	hash =hashlib.md5()
	for i in xrange(10):
		hash.update(result+salt)
		result =	hash.hexdigest()
	return salt + result

def validate_password(hashed,input_password):

	return hashed == encrypt_password(input_password,salt=hashed[:8])


if __name__ == '__main__':
	hashed = encrypt_password('secret password')
	print hashed
	assert validate_password(hashed,'secret password')
	# for test !