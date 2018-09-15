Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # This is comment
>>> print ("Hello,world!")
Hello,world!
>>> 

>>> #対角線の長さ
>>> import math
>>> l = 4
>>> w = 10
>>> d = math.sqrt(1**2 + w**2)
>>> 
>>> print ("d")
d
>>> print d
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(d)?
>>> print ("Python")
Python
>>> print ("こんにちは!")
こんにちは!
>>> print ("""これは、とても、とても、とても長い複数行のコードです。"""
	   )
これは、とても、とても、とても長い複数行のコードです。
[
>>> これは、とても、とても、とても長い複数行のコードです。
SyntaxError: invalid character in identifier
>>> print/
SyntaxError: invalid syntax
>>> print\
("""これは、とても、とても、とても
長い複数行のコードです
。""")
これは、とても、とても、とても
長い複数行のコードです
。
>>> 
