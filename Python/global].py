Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 100
>>> 
>>> def f():
	global x
	x += 1
	print(x)

	
>>> f()
101
>>> #ローカルスコープからグローバル変数に書き込むためにはglobalを使う
