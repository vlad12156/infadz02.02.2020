Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> arr = []
>>> a1 = random.sample(range(4,10),5)
>>> a2 = random.sample(range(4,10),5)
>>> a = (a1,a2)
>>> arr.append(a)
>>> print(a)
([4, 9, 7, 5, 6], [7, 4, 5, 6, 8])
>>> b = (a1 + a2)
>>> print(sum(b))
61
>>> 