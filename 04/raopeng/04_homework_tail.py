#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    author: RaoPeng

import time
#未完成
def tail(file_name):
	FILE_START = 0
	FILE_NOW = 1
	FILE_END = 2
	with open(file_name) as f:
		while True:
			f.seek(FILE_END)
			if line:
				return line
			else:
				time.sleep(1)

print tail('log')
