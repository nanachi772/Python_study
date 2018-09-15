Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("ひらがな")
ひらがな
>>> print ("かたかな")
かたかな
>>> print ("漢字")
漢字
>>> value = "5"
>>> if value <= 10:
	print ("10未満です")
else:
	print ("10以上です")

	
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    if value <= 10:
TypeError: '<=' not supported between instances of 'str' and 'int'
>>> if int(value) <= 10:
	print ("10未満です")
else:
	print ("10以上です")

	
10未満です
>>> value = "26"
>>> if int(value) <= 10:
	print ("10以下")
elif int(value) > 10 and int(value) <= 25:
	print ("10より大きく25以下")
else:
	print ("25より大きい")

	
25より大きい
>>> 10 % 3
1
>>> 10 / 3
3.3333333333333335
>>> age = "20"
>>> if int(age) < 20:
	print ("二十歳未満")
else:
	print ("成年")

	
成年
>>> 
