Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def f(x=2):
	return x ** x

>>> print f():
	
SyntaxError: invalid syntax
>>> print (f():)
SyntaxError: invalid syntax
>>> print (f())
4
>>> print (f(4))
256
>>> 
>>> def add_it(x, y=10):
	return x + y

>>> result = add_it(2)
>>> print (result)
12
>>> print (add_it(2))
12
>>> 
