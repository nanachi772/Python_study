Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> age = input("Enter your age")
Enter your age23
>>> int_age = int(age)
>>> if age < 21:
	print("You are young")
else:
	print("Wow, you are old!")

	
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    if age < 21:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> if int_age < 21:
	print("You are young")
else:
	print("Wow, you are old!")

	
Wow, you are old!
>>> 
