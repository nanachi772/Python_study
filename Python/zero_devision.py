Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = input("type a number:")
type a number:10
>>> b = input("type another:")
type another:5
>>> a = int(a)
>>> b = int(b)
>>> print (a / b)
2.0
>>> 
>>> a = input("type a number")
type a number10
>>> b = input("type another")
type another0
>>> a = int(a)
>>> b = int(b)
>>> print (a / b)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print (a / b)
ZeroDivisionError: division by zero
>>> 
