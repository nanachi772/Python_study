Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def f(x):
	f(2)
	result = f(2)
print(result)
SyntaxError: invalid syntax
>>> 
>>> def f(x):
	return x * 2
f(2)
SyntaxError: invalid syntax
>>> def f(x):
	return x * 2
	f(2)
	result = f(2)

	
>>> print(result)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(result)
NameError: name 'result' is not defined
>>> print (result)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print (result)
NameError: name 'result' is not defined
>>> def f(x):
	return x * 2

>>> f(2)
4
>>> result = f(2)
>>> print (result)
4
>>> print(result)
4
>>> def f(x)]
SyntaxError: invalid syntax
>>> def f(x):
	return x + 1

>>> z = f(4)
>>> if z == 5:
	print ("zは5")
else:
	print ("z is not 5")

	
zは5
>>> def f():
	return 1 + 1

>>> print f()
SyntaxError: invalid syntax
>>> print (f())
2
>>> def f(x , y , z)
SyntaxError: invalid syntax
>>> def f(x , y , z):
	return x + y + z

>>> result = f(1 , 2 , 3)
>>> print(result


	  )
6
>>> def f():
	return

>>> result = f(4)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    result = f(4)
TypeError: f() takes 0 positional arguments but 1 was given
>>> result = f()
>>> print(result)
None
>>> len("monty")
5
>>> len("Python")
6
>>> str(100)
'100'
>>> int("1")
1
>>> int("110")
110
>>> int("6.4")
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int("6.4")
ValueError: invalid literal for int() with base 10: '6.4'
>>> int(20.54)
20
>>> float("16.4")
16.4
>>> float(99)
99.0
>>> int("princess")
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    int("princess")
ValueError: invalid literal for int() with base 10: 'princess'
>>> 
