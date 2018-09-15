def multipiler(x):
    return x ** 2
    """
    return x ** 2.
    :param x: int.
    :param y: int.
    """
print(multipiler(3))

#二問
def string(word):
    print (word)
word = "Today is rainy"
string(word)

#3問
def five(a, b, c, d=4, f=5):
    return a + b + c + d + f
print (five(1, 2, 3))

#4問
def one(x):
    return (x // 2)

def two(y):
    return (y * 4)

print (one(12))
print (two(40))
three = one(6)
print (two(three))

#4問
def spider(x):
    return float(x)
try:
    result = spider("miss")
    print (result)
except (ZeroDivisionError, ValueError):
    print ("Invalid input.")

def test(x):
    print (float(x))
test(11)
