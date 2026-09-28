Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> male=50
>>> female=60
>>> print(female <=30 and male >=50)
False
>>> print(female <=60 and male <=50)
True
>>> print(female >=60 and male <=20)
False
>>> print( not (male<50)and (female<50))
False
>>> print(not (male<40) and (female<50))
False
>>> print(not (male<55) or (female>20))
True
>>> 
>>> shopname='d mart'
>>> revenue=500000
>>> employees=100
>>> branch=4
>>> print( shopname == 'd mart' and revenue <= 500000 and employees <=100 and branch <=4)
True
>>> print(revenue < 500000 or branch >4)
False
>>> print(revenue < 500000 or branch <4)
False
