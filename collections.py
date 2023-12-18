# TODO: Collections in python
# TODO: Array declaration in python

from collections import Counter
# 1. Counters

# A counter is a sub-class of the dictionary. 
# It is used to keep the count of the elements in an iterable in the form of an 
# unordered dictionary where the key represents the element in the iterable and 
# value represents the count of that element in the iterable.
# With sequence of items 
print(Counter(['B','B','A','B','C','A','B', 
			'B','A','C'])) 
	
# with dictionary 
print(Counter({'A':3, 'B':5, 'C':2})) 
	
# with keyword arguments 
print(Counter(A=3, B=5, C=2))


# 2. OrderedDict
# An OrderedDict is also a sub-class of dictionary but unlike dictionary, 
# it remembers the order in which the keys were inserted. 



# OrderedDict
# DefaultDict
# ChainMap
# NamedTuple
# DeQue
# UserDict
# UserList
# UserString

