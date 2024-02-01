Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list = ["orange", "apple", "banana", "pear", "cherry"]
>>> my_list[3]
'pear'
>>> my_list[0]
'orange'
>>> my_tuple = ("2", "4", "6", "8")
>>> my_tuple.index("4")
1
>>> my_tuple.index("8")
3
>>> fruits = {"apple", "banana", "cherry", "watermelon", "orange"}
>>> vegetables = {"carrot", "tomato", "pepper"}
>>> fruits.union(vegetables)
{'apple', 'pepper', 'orange', 'watermelon', 'cherry', 'banana', 'carrot', 'tomato'}
>>> fruits.intersection(vegetables)
set()
