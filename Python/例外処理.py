Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = input("type a number")
type a number10
>>> b = input("type anorher")
type anorher0
>>> a = int(a)
>>> b = int(b)
>>> try:
	print (a / b)
except ZeroDivisionError:
	print ("b cannot be zero")

	
b cannot be zero
>>> 
