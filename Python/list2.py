Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fruit = list()
>>> fruit
[]
>>> fruit = []
>>> fruit
[]
>>> fruit = ["Apple", "Orange", "Pear"]
]
>>> fruit
['Apple', 'Orange', 'Pear']
>>> fruit.append("Banana")
>>> fruit.append("Peach")
>>> fruit
['Apple', 'Orange', 'Pear', 'Banana', 'Peach']
>>> 
>>> random = []
>>> random.append(True)
>>> random.append(100)
>>> random.append(1.1)
>>> random.append("Hello")
>>> random
[True, 100, 1.1, 'Hello']
>>> fruit[1]
'Orange'
>>> fruit[4]
'Peach'
>>> fruit[5]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    fruit[5]
IndexError: list index out of range
>>> colors = ["blue", "green", "yellow"]
>>> colors
['blue', 'green', 'yellow']
>>> colors[2] = "red"
>>> colors
['blue', 'green', 'red']
>>> item = colors.pop()
>>> item
'red'
>>> colors
['blue', 'green']
>>> colors2 = ["orange", "pink", "black"]
>>> colors + colors2
['blue', 'green', 'orange', 'pink', 'black']
>>> green in  colors
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    green in  colors
NameError: name 'green' is not defined
>>> "green" in colors
True
>>> "black" not in colors
True
>>> len(colors)
2
>>> len(colors2)
3
>>> len(colors + colors2)
5
>>> colors = ["purple", "orange", "green"]
>>> 
>>> guess = input("何色でしょう？（入力してください）:")
何色でしょう？（入力してください）:
>>> if guess in colors:
	priont ("大当たり")

>>> 
