Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("hello world")
hello world
>>> name = input("Enter your name:")
Enter your name:zhangzhu
>>> print(name)
zhangzhu
>>> "hello" + "world"
'helloworld'
>>> 'hello' + 'world'
'helloworld'
>>> 10//3
3
>>> 2**3
8
>>> x,y,z = 1,2,"zhangsan"
>>> print(x)
1
>>> print(z)
zhangsan
>>> """
床前明月光
疑是地上霜
"""
'\n床前明月光\n疑是地上霜\n'
>>> print("床前明月光\n疑是地上霜")
床前明月光
疑是地上霜
>>> m = 1;n = "A"
>>> print("%d is a number,%s is a string" %(m,n))
1 is a number,A is a string
>>> l = [1,2,3]
>>> print("这个列表内容是%r" % l)
这个列表内容是[1, 2, 3]
>>> "hello" * 2
'hellohello'
>>> print(r"中间有换行符\n前面的r起作用\对后边")
中间有换行符\n前面的r起作用\对后边
>>> clear
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> s.count("weeieii")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.count("weeieii")
NameError: name 's' is not defined
>>> str.count("weeli")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    str.count("weeli")
TypeError: count() takes at least 1 argument (0 given)
>>> str.count("a")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    str.count("a")
TypeError: count() takes at least 1 argument (0 given)
>>> str.count("n")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    str.count("n")
TypeError: count() takes at least 1 argument (0 given)
>>> s = "werqwer"
>>> s.count("w")
2
>>> s.endswith(w,e,r)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s.endswith(w,e,r)
NameError: name 'w' is not defined
>>> A=[10,11,12,13]
>>> B=["red","blue","green"]
>>> C=[]
>>> E=A+B
>>> L=[1,2,3,[4,5,6]]
>>> b=A[1]
>>> print(b)
11
>>> A[2]=5
>>> print(A[2])
5
>>> print(L[3][1])
5
>>> print(A[0:2])
[10, 11]
>>> print(A[-3:-1])
[11, 5]
>>> print(A[-2])
5
>>> len(L)
4
>>> len(A)
4
>>> max(A)
13
>>> A.append(14)
>>> print(A)
[10, 11, 5, 13, 14]
>>> A.append(5)
>>> print(A)
[10, 11, 5, 13, 14, 5]
>>> A.index(5)
2
>>> A.pop()
5
>>> print(A)
[10, 11, 5, 13, 14]
>>> A.reverse()
>>> print(A)
[14, 13, 5, 11, 10]
>>> A.sort()
>>> print(A)
[5, 10, 11, 13, 14]
>>> L1=A
>>> print(L1)
[5, 10, 11, 13, 14]
>>> L1=A.copy()
>>> print(L1)
[5, 10, 11, 13, 14]
>>> L2=A.copy()
>>> print(L2)
[5, 10, 11, 13, 14]
>>> L2.clear()
>>> print(L2)
[]
>>> L1=L2.copy()
>>> print(L1)
[]
>>> A.insert(2,18)
>>> print(A)
[5, 10, 18, 11, 13, 14]
>>> print(A)
[5, 10, 18, 11, 13, 14]
>>> l1=A
>>> print(A)
[5, 10, 18, 11, 13, 14]
>>> A.append(15)
>>> print(l1)
[5, 10, 18, 11, 13, 14, 15]
>>> a="hello world"
>>> print(a[6])
w
>>> print(a[3:8])
lo wo
>>> print(a[-5:-2])
wor
>>> print("w"not in a)
False
>>> print("z"not in a)
True
>>> M=['a','b','c']
>>> print("".join(M))
abc
>>> print("_".join(M))
a_b_c
>>> N='he llo wor ld'
>>> N.strip()
'he llo wor ld'
>>> N=' he llo wor ld '
>>> N.strip()
'he llo wor ld'
>>> N=' he llo wor ld '
>>> N.rstrip()
' he llo wor ld'
>>> N.find(o)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    N.find(o)
NameError: name 'o' is not defined
>>> N.find('o')
6
>>> N.rfind('o')
9
>>> N.find("dd")
-1
>>> M=['a','b','c',1,2,3]
>>> print("".join(M))
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    print("".join(M))
TypeError: sequence item 3: expected str instance, int found
>>> N.find('o',0,7)
6
>>> N.endswith('o',0,6)
False
>>> N.endswith('o',0,7)
True
>>> print(N)
 he llo wor ld 
>>> N.split('o',num=string.count(N))
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    N.split('o',num=string.count(N))
NameError: name 'string' is not defined
>>> N.startswith('o',6,9)
True
>>> N.startswith('o',7,9)
False
>>> N.split('o')
[' he ll', ' w', 'r ld ']
>>> f = (1,2,3,4)
>>> f.append(5)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    f.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> f=(1)
>>> print(f)
1
>>> f.append(5)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    f.append(5)
AttributeError: 'int' object has no attribute 'append'
>>> c={'uid':105,
   'login':'admin',
   'passwd':'123 zz'
   }
>>> u=c['uid']
>>> print(u)
105
>>> c['login']='zhangsan'
>>> print(c['login'])
zhangsan
>>> print(c)
{'uid': 105, 'login': 'zhangsan', 'passwd': '123 zz'}
>>> c['name']='wangwu'
>>> print(c)
{'uid': 105, 'login': 'zhangsan', 'passwd': '123 zz', 'name': 'wangwu'}
>>> len(c)
4
>>> c.get('uid',default='存在')
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    c.get('uid',default='存在')
TypeError: get() takes no keyword arguments
>>> c.get('uid','存在')
105
>>> c.get('u','存在')
'存在'
>>> c.get('u','不存在')
'不存在'
>>> c.setdefault('uid','不存在')
105
>>> c.setdefault('new','不存在')
'不存在'
>>> print(c)
{'uid': 105, 'login': 'zhangsan', 'passwd': '123 zz', 'name': 'wangwu', 'new': '不存在'}
>>> 'uid' in c
True
>>> 'id' in c
False
>>> c.items()
dict_items([('uid', 105), ('login', 'zhangsan'), ('passwd', '123 zz'), ('name', 'wangwu'), ('new', '不存在')])
>>> c.items('passwd','123 zz')
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    c.items('passwd','123 zz')
TypeError: items() takes no arguments (2 given)
>>> c.keys()
dict_keys(['uid', 'login', 'passwd', 'name', 'new'])
>>> c.values()
dict_values([105, 'zhangsan', '123 zz', 'wangwu', '不存在'])
>>> c.pop('new',"李四')
      
SyntaxError: EOL while scanning string literal
>>> c.pop('new','李四')
'不存在'
>>> print(c)
{'uid': 105, 'login': 'zhangsan', 'passwd': '123 zz', 'name': 'wangwu'}
>>> c.pop('new','李四')
'李四'
>>> print(c)
{'uid': 105, 'login': 'zhangsan', 'passwd': '123 zz', 'name': 'wangwu'}
>>> 
>>> if y>0:
	print('y>0')
elif y==0:
	print('y==0)
	      
SyntaxError: EOL while scanning string literal
>>> if y>0:
	print('y>0')
elif y==0:
	print('y==0')
else:
	print('y<0')

	
y>0
>>> a=2;b=4;c=5
>>> if b>=a and b<=c:
	print('b is between a and c')
if not(b<a or b>c):
	
SyntaxError: invalid syntax
>>>  if b>=a and b<=c:
	print('b is between a and c')
	
SyntaxError: unexpected indent
>>> if b>=a and b<=c:
	print('b is between a and c')

	
b is between a and c
>>> if not(b<a or b>c):
	print('b is still between a and c')

	
b is still between a and c
>>> range(10)
range(0, 10)
>>> print(range(10))
range(0, 10)
>>> range(1,10,2)
range(1, 10, 2)
>>> i=5
>>> while i>0:
	print('hello world ! %d' %i)
	i=i-1

	
hello world ! 5
hello world ! 4
hello world ! 3
hello world ! 2
hello world ! 1
>>> for i in [3,4,5,10,25]:
	print(i)

	
3
4
5
10
25
>>> for c in 'hello world':
	print(c)

	
h
e
l
l
o
 
w
o
r
l
d
>>> O = [1,3,4,5,7,9]
>>> for i in range(len(O)):
	print(i)

	
0
1
2
3
4
5
>>> for i in range(len(O)):
	print(O[i])

	
1
3
4
5
7
9
>>> C = input('请输入：'):
	
SyntaxError: invalid syntax
>>> C = input('请输入：');
请输入：2
>>> C = input('请输入：');print('你输入的内容是：',C)
请输入：2
你输入的内容是： 2
>>> while i**2 >50:
	print('i=',i)
i= input('请输入：')
SyntaxError: invalid syntax
>>> i = input('请输入：');
请输入：
>>> i = input('请输入：');while i**2 >50:
	
SyntaxError: invalid syntax
>>> while i<50:
	a = input('请输入：')
	i=a**2
	print('i=',i)

	
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    while i<50:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> while i<50:
	a = input('请输入：')
	i=a**2
	print i
	
SyntaxError: Missing parentheses in call to 'print'
>>> while i<50:
	a = input('请输入：')
	i=a**2
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    while i<50:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> while i<50:
	a=int(input('请输入：'))
	i=a**2
	print(i)

	
Traceback (most recent call last):
  File "<pyshell#194>", line 1, in <module>
    while i<50:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> while i<50:
	a=int(input('请输入：'))
	i=a**2
	print i
	
SyntaxError: Missing parentheses in call to 'print'
>>> while i<50:
	i=int(input('请输入：'))
	print(i**2)

	
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    while i<50:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> while i < 50:
	i=int(input('请输入：'))
	print(i**2)

	
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    while i < 50:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> while i < 50:
	i=int(input('请输入：'))
	print(i**2)

	
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    while i < 50:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> while i < 50:
	i = 1
	i=int(input('请输入：'))
	print(i**2)

	
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    while i < 50:
TypeError: '<' not supported between instances of 'str' and 'int'
>>> i = 1
>>> while i < 50:
	i=int(input('请输入：'))
	print(i**2)

	
请输入：2
4
请输入：5
25
请输入：
Traceback (most recent call last):
  File "<pyshell#210>", line 2, in <module>
    i=int(input('请输入：'))
ValueError: invalid literal for int() with base 10: ''
>>> i=1
>>> while i < 50:
	i=int(input('请输入：'))
	print(i**2)

	
请输入：2
4
请输入：5
25
请输入：7
49
请输入：8
64
请输入：9
81
请输入：
Traceback (most recent call last):
  File "<pyshell#213>", line 2, in <module>
    i=int(input('请输入：'))
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> i=1
>>> while a < 50:
	a=i**2
	i=int(input('请输入：'))
	print(a)

	
请输入：2
1
请输入：5
4
请输入：9
25
请输入：166
81
>>> i=1
>>> while a < 50:
	i=int(input('请输入：'))
	a=i**2
	print(a)

	
>>> while a < 50:
	i=int(input('请输入：'))
	a=i**2
	print(a)

	
>>> S=[3,5,7,9]
>>> def add(p1,p2):
	print('%d + %d = %d' %(p1,p2,p1+p2))

	
>>> add(1,2)
1 + 2 = 3
>>> def divide(a,b):
	q=a/b
	r=a-q*b
	return q,r

>>> x,y=divide(42,5)
>>> print(x,y)
8.4 0.0
>>> print(x)
8.4
>>> print(y)
0.0
>>> del func(name,score=90)
SyntaxError: can't delete function call
>>> def func(name,score=90)
SyntaxError: invalid syntax
>>> def func(name,score=90):
	print(name)
	print(score)

	
>>> func(,88)
SyntaxError: invalid syntax
>>> def func(name,score=90):
	print('%name 的成绩是%score' %(name,score))

	
>>> func('张三')
Traceback (most recent call last):
  File "<pyshell#247>", line 1, in <module>
    func('张三')
  File "<pyshell#246>", line 2, in func
    print('%name 的成绩是%score' %(name,score))
ValueError: unsupported format character 'n' (0x6e) at index 1
>>> func('张三',88)
Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    func('张三',88)
  File "<pyshell#246>", line 2, in func
    print('%name 的成绩是%score' %(name,score))
ValueError: unsupported format character 'n' (0x6e) at index 1
>>> def func(name,score):
	print('%name 的成绩是%score' %(name,score))

	
>>> func('张三',80)
Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    func('张三',80)
  File "<pyshell#250>", line 2, in func
    print('%name 的成绩是%score' %(name,score))
ValueError: unsupported format character 'n' (0x6e) at index 1
>>> def func(name,score):
	print('%n 的成绩是%s' %(name,score))

	
>>> func('张三',80)
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    func('张三',80)
  File "<pyshell#253>", line 2, in func
    print('%n 的成绩是%s' %(name,score))
ValueError: unsupported format character 'n' (0x6e) at index 1
>>> def func(name,score):
	print('%s 的成绩是%d' %(name,score))

	
>>> func('张三',80)
张三 的成绩是80
>>> def func(name,score):
	print('%r的成绩是%r' %(name,score))

	
>>> func('张三',80)
'张三'的成绩是80
>>> def func(*f):
	print(f)

	
>>> func(a)
(81,)
>>> func(221,22,44,55,44)
(221, 22, 44, 55, 44)
>>> func(1)
(1,)
>>> func(A)
([5, 10, 18, 11, 13, 14, 15],)
>>> t=('lisi',80)
>>> def func(name,score):
	print('%r的成绩是%r' %(name,score))

	
>>> func(*t)
'lisi'的成绩是80
>>> func(t)
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    func(t)
TypeError: func() missing 1 required positional argument: 'score'
>>> def func(*args):
	sum=0
	for n in args:
		sum = sum+n
	return sum

>>> func(32)
32
>>> func(32,2)
34
>>> def func(name,age=20):
	print("%s 's age is%d" %(name,age))

	
>>> person=('name':'Bob','age':27)
SyntaxError: invalid syntax
>>> person=('name':"Bob",'age':27)
SyntaxError: invalid syntax
>>> person={'name':"Bob",'age':27}
>>> func(**person)
Bob 's age is27
>>> def func(**kw):
	print(**kw)

	
>>> func(a=1,b=2,c=3)
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    func(a=1,b=2,c=3)
  File "<pyshell#290>", line 2, in func
    print(**kw)
TypeError: 'a' is an invalid keyword argument for this function
>>> class Count():
	def__init__(self,a,b):
		
SyntaxError: invalid syntax
>>> class Count():
	def_init_(self,a,b):
		
SyntaxError: invalid syntax
>>> class Count():
	def_ _init_ _(self,a,b):
		
SyntaxError: invalid syntax
>>> class Count():
	def __init__(self,a,b):
		self.a=a
		self.b=b
		def add(self):
			return self.a + self.b

		
>>> count = Count(3,7)
>>> count.add()
Traceback (most recent call last):
  File "<pyshell#303>", line 1, in <module>
    count.add()
AttributeError: 'Count' object has no attribute 'add'
>>> Count.add()
Traceback (most recent call last):
  File "<pyshell#304>", line 1, in <module>
    Count.add()
AttributeError: type object 'Count' has no attribute 'add'
>>> class Count():
	def __init__(self,a,b):
		self.a=a
		self.b=b

	def add(self):
		return self.a + self.b

	
>>> count = Count(3,7)
>>> count.add()
10
>>> class Count():
	def add(self,a,b):
		return a+b

	
>>> count=Count()
>>> count.add(3,5)
8
>>> class Father():
	def __init__(self,a,b)
	
SyntaxError: invalid syntax
>>> class Father():
	def __init__(self,a,b):
		self.a=a
		self.b=b
	def add(self):
		return self.a + self.b
	def sub(self):
		return self.a - self.b

	
>>> class Son(Father):                      #申明子类，继承父类
	def print__add(self):
		print(self.add())           #调用父类的方法
	def sub(self):                      #重写父类同名方法
		return self.a*2 - self.b    #调用父类属性

	
>>> son = Son(6,3)
>>> son.add()
9
>>> son.sub()
9
>>> son.sub()
9
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
