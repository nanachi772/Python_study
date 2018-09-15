Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 2
>>> if x ==2:
	print ("数値は2です")
if x % 2 == 0:
	
SyntaxError: invalid syntax
>>> x = 2
>>> if x ==2:
	print ("数値は2です")

数値は2です
>>> if x % 2 == 0
SyntaxError: invalid syntax
>>> if x % 2 == 0:
	print ("数値は偶数です")
if x % 2 != 0:
	
SyntaxError: invalid syntax
>>> if x % 2 == 0:
	print ("数値は偶数です")

	
数値は偶数です
>>> if x % 2 != 0:
	print ("数値は奇数です")

	
>>> x = 10
>>> y = 11
>>> if x == 10:
	if y == 11:
		print (x + y)

		
21
>>> home = "タイ"
>>> if home == "日本":
	print ("Hello,Japan!")
elif home == "タイ":
	print ("Hello,Thailand!")
elif home == "インド":
	print ("Hello,India!")
elif home == "中国":
	print ("Hello,China!")
else:
	print ("Hello,World!")

	
Hello,Thailand!
>>> 
