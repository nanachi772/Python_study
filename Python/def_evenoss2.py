Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def even_odd():
	n = input("Type a number")
	n = int(n)
	if n % 2 == 0:
		print ("n is even.")
	else:
		print ("n is odd")

		
>>> even_odd()
Type a number3
n is odd
>>> even_odd()
Type a number721
n is odd
>>> even_odd()
Type a number920312
n is even.
>>> 
