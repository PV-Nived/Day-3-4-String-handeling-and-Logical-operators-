Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name='john'
name.capitalize()
'John'
name.casefold()
'john'
name.center()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    name.center()
TypeError: center expected at least 1 argument, got 0

===== RESTART: C:/Users/Nived/Downloads/day 3.py =====
name
'john'
name='john'
name.capitalize()
'John'
name.casefold()
'john'
name.center(14)
'     john     '
name.count('j')
1
>>> name.encode('utf-16')
b'\xff\xfej\x00o\x00h\x00n\x00'
>>> name.encode('utf-8')
b'john'
>>> name.endswith('n')
True
>>> name.endswith('h')
False
>>> name.find('h')
2
>>> #j o h n
>>> #0 1 2 3
>>> 
>>> name=john
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    name=john
NameError: name 'john' is not defined
>>> name='john'
>>> 'my name is {}'.format('john')
'my name is john'
>>> 'my name is {name}'.format_map({'name': 'charlie'})
'my name is charlie'
>>> name='john'
>>> 
>>> name='nived kumar'
>>> name.index('k')
6
>>> name.index(' ')
5
