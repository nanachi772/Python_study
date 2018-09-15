Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_tuple = tuple()
>>> my_tuple
()
>>> rndm = ("M.Jackson", 1958, True)
>>> rndm
('M.Jackson', 1958, True)
]
>>> #こ
>>> 
>>> 
>>> ("self_taught")
'self_taught'
>>> dys = ("1984", "Brave New World", "Fahrenheit 451")
>>> dys[1] = "Handmaid's Tale"
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    dys[1] = "Handmaid's Tale"
TypeError: 'tuple' object does not support item assignment
>>> dys[2]
'Fahrenheit 451'
>>> "1984" in dys
True
>>> fruit = ["Apple": "Red", "Banana":"Yellow":]
SyntaxError: invalid syntax
>>> fruits = ["Apple":"Red", "Banana":"Yellow":]
SyntaxError: invalid syntax
>>> fruits = ["Apple"ed", "Banana":"Yellow":]
	      
SyntaxError: invalid syntax
>>> fruits = ["Apple":"Red", "Banana":"Yellow":]
	      
SyntaxError: invalid syntax
>>> fruits = ["Apple":"Red", "Banana":"Yellow"]
	      
SyntaxError: invalid syntax
>>> fruits = ["Apple":"Red", "Banana":"Yellow"]
	      
SyntaxError: invalid syntax
>>> fruits = ["Apple": "Red", "Banana": "Yellow"]
	      
SyntaxError: invalid syntax
>>> fruits = {"Apple": "Red", "Banana": "Yellow"}
	      
>>> fruuit
	      
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    fruuit
NameError: name 'fruuit' is not defined
>>> fruit
	      
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    fruit
NameError: name 'fruit' is not defined
>>> fruits
	      
{'Apple': 'Red', 'Banana': 'Yellow'}
>>> facts = dict()
	      
>>> facts{"code"} = "fun"
	      
SyntaxError: invalid syntax
>>> fact["code"] = "fun"
	      
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    fact["code"] = "fun"
NameError: name 'fact' is not defined
>>> facts["code"] = "fun"
	      
>>> facts
	      
{'code': 'fun'}
>>> facts["Bill"] = "Gates"
	      
>>> facts
	      
{'code': 'fun', 'Bill': 'Gates'}
>>> facts["code"] = "fuuuuun"
	      
>>> facts
	      
{'code': 'fuuuuun', 'Bill': 'Gates'}
>>> facts["founded"] = 1776
	      
>>> facts
	      
{'code': 'fuuuuun', 'Bill': 'Gates', 'founded': 1776}
>>> bill = {"Bill Gates": "charitable"}
	      
>>> "Bill Gates" in bill
	      
True
>>> print bill
	      
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(bill)?
>>> bill
	      
{'Bill Gates': 'charitable'}
>>> books = {"Dracula": "Stoker",
	     "1984": "Oewell",
	     "The Trial": "Kafka"}
	      
>>> books
	      
{'Dracula': 'Stoker', '1984': 'Oewell', 'The Trial': 'Kafka'}
>>> del books{"The Trial"}
	      
SyntaxError: invalid syntax
>>> del books {"The Trial"}
	      
SyntaxError: invalid syntax
>>> del books ["The Trial"]
	      
>>> books
	      
{'Dracula': 'Stoker', '1984': 'Oewell'}
>>> 
