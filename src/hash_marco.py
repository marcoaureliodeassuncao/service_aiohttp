# -*- coding: utf-8 -*-
import hashlib
import sys


def hash_md5(pwd):
	return str(hashlib.md5(pwd.encode('utf-8')).digest())


def hash_sha256(pwd):
	return str(hashlib.sha256(pwd.encode('utf-8')).digest())


if __name__ == '__main__':

	print(hash_md5(sys.argv[1]))
	print(hash_sha256(sys.argv[1]))
