
a = input("type a number:")
b = input("type anorher:")
a = int(a)
b = int(b)
try:
	print (a / b)
except (ZeroDivisionError, ValueError):
	print ("b cannot be zero")
	
