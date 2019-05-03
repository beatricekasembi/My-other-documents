Python 3.8.0a1 (tags/v3.8.0a1:e75eeb00b5, Feb  3 2019, 20:47:39) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Number = [1,2,3,4,5,6,7,8,9]
>>> Number
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for x in Numbers
SyntaxError: invalid syntax
>>> for x in Numbers:
	sum.print(x+x)

	
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    for x in Numbers:
NameError: name 'Numbers' is not defined
>>> for x in Number:
	sum.print(x+x)

	
Traceback (most recent call last):
  File "<pyshell#7>", line 2, in <module>
    sum.print(x+x)
AttributeError: 'builtin_function_or_method' object has no attribute 'print'
>>> for x in Number:
	print(x+x)

	
2
4
6
8
10
12
14
16
18
>>> for x in range of(0,100):
	if x%9==0
	
SyntaxError: invalid syntax
>>> for x in range(0,100):
	if x%9==0:
		print(x)

		
0
9
18
27
36
45
54
63
72
81
90
99
>>> for x in range(0,100):
	if x%7==0:
		print(x)

		
0
7
14
21
28
35
42
49
56
63
70
77
84
91
98
>>> for x in range(0,10):
	print dict
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(dict)?
>>> for x in range(0,10):
	print (dict)

	
<class 'dict'>
<class 'dict'>
<class 'dict'>
<class 'dict'>
<class 'dict'>
<class 'dict'>
<class 'dict'>
<class 'dict'>
<class 'dict'>
<class 'dict'>
>>> a = range(0,10)
>>> a
range(0, 10)
>>> for x in a:
	print(a)

	
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
range(0, 10)
>>> for x in range(0,10):
	print(x**3)

	
0
1
8
27
64
125
216
343
512
729
>>> 
for x in range(0,10):
	print(x, x**3)

	
0 0
1 1
2 8
3 27
4 64
5 125
6 216
7 343
8 512
9 729
>>> def beaty(number):
	y=[]
	for x in range(1,number):
		y.append x
		
SyntaxError: invalid syntax
>>> def beaty(number):
	y=[]
	for x in range(1,number):
		y.append(x)
		z=sum(y)

		
>>> print z
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(z)?
>>> print(z)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
>>> print z
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(z)?
>>> print (z)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print (z)
NameError: name 'z' is not defined
>>> def beaty(number):
	y=[]
	for x in range(1,number):
		y.append(x)
		z=sum(y)
	return z

>>> beaty(20)
190
>>> def beaty(number):
	y=[]
	for x in range(1,number):
		y.append(x)
		z=sum(y)
	return z

>>> beaty(50)
1225
>>> def data(list,x,y)
SyntaxError: invalid syntax
>>> def data(list,a,b):
	a=[]
	b=[]
	for x in list:
		if x%a==0:
		elif
		
SyntaxError: expected an indented block
>>> def data(list,a,b):
	a=[]
	b=[]
	for x in list:
		if x%a==0:
			a.append(x)
		elif x%b==0:
			b.append(x)
	print(a)
	print(b)

	
>>> list(6,10)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    list(6,10)
TypeError: list expected at most 1 argument, got 2
>>> data(range(0,10),2,3)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    data(range(0,10),2,3)
  File "<pyshell#59>", line 5, in data
    if x%a==0:
TypeError: unsupported operand type(s) for %: 'int' and 'list'
>>> def data(list,x,y):
	a=[]
	b=[]
	for z in list:
		if z%x==0:
			a.append(z)
		elif z%y==0:
			b.append(z)
	print(a)
	print(b)

	
>>> data(range(0,10),2,3)
[0, 2, 4, 6, 8]
[3, 9]
>>> data(range(0,100),5,7)
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
[7, 14, 21, 28, 42, 49, 56, 63, 77, 84, 91, 98]
>>> dict m=[]
SyntaxError: invalid syntax
>>> m=dict[]
SyntaxError: invalid syntax
>>> m=dict[]
SyntaxError: invalid syntax
>>> m=dict()
>>> m
{}
>>> def function(range (0,10)):
	
SyntaxError: invalid syntax
>>> def function(range(0,10)):
	
SyntaxError: invalid syntax
>>> def function(range 0,10):
	
SyntaxError: invalid syntax
>>> for x in range (0,10):
	print(x**3)

	
0
1
8
27
64
125
216
343
512
729
>>> for x in range (0,10):
	z=(x),(x**3)
	print(m)

	
{}
{}
{}
{}
{}
{}
{}
{}
{}
{}
>>> a=dict()
>>> for x in range (0,10):
	a[x]:x**3

	
>>> a
{}
>>> for x in range (0,10):
	a[x]=x**3

	
>>> g
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    g
NameError: name 'g' is not defined
>>> a
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
>>> for x in range (0,100):
	a[x]=x**3

	
>>> g
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    g
NameError: name 'g' is not defined
>>> for x in range (0,100):
	m[x]=x**3

	
>>> m
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000, 11: 1331, 12: 1728, 13: 2197, 14: 2744, 15: 3375, 16: 4096, 17: 4913, 18: 5832, 19: 6859, 20: 8000, 21: 9261, 22: 10648, 23: 12167, 24: 13824, 25: 15625, 26: 17576, 27: 19683, 28: 21952, 29: 24389, 30: 27000, 31: 29791, 32: 32768, 33: 35937, 34: 39304, 35: 42875, 36: 46656, 37: 50653, 38: 54872, 39: 59319, 40: 64000, 41: 68921, 42: 74088, 43: 79507, 44: 85184, 45: 91125, 46: 97336, 47: 103823, 48: 110592, 49: 117649, 50: 125000, 51: 132651, 52: 140608, 53: 148877, 54: 157464, 55: 166375, 56: 175616, 57: 185193, 58: 195112, 59: 205379, 60: 216000, 61: 226981, 62: 238328, 63: 250047, 64: 262144, 65: 274625, 66: 287496, 67: 300763, 68: 314432, 69: 328509, 70: 343000, 71: 357911, 72: 373248, 73: 389017, 74: 405224, 75: 421875, 76: 438976, 77: 456533, 78: 474552, 79: 493039, 80: 512000, 81: 531441, 82: 551368, 83: 571787, 84: 592704, 85: 614125, 86: 636056, 87: 658503, 88: 681472, 89: 704969, 90: 729000, 91: 753571, 92: 778688, 93: 804357, 94: 830584, 95: 857375, 96: 884736, 97: 912673, 98: 941192, 99: 970299}
>>> 
