# TODO: Collections in python
# TODO: Array declaration in python

from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import ChainMap
# 1. Counters

# A counter is a sub-class of the dictionary. 
# It is used to keep the count of the elements in an iterable in the form of an 
# unordered dictionary where the key represents the element in the iterable and 
# value represents the count of that element in the iterable.
# With sequence of items 
print("Counter---------")
print(Counter(['B','B','A','B','C','A','B', 
			'B','A','C'])) 
	
# with dictionary 
print(Counter({'A':3, 'B':5, 'C':2})) 
	
# with keyword arguments 
print(Counter(A=3, B=5, C=2))


# 2. OrderedDict
# An OrderedDict is also a sub-class of dictionary but unlike dictionary, 
# it remembers the order in which the keys were inserted. 
print("OrderedDict------------")
od = OrderedDict()  
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
    
print('Before Deleting') 
for key, value in od.items():  
    print(key, value)  
      
# deleting element 
od.pop('a') 
  
# Re-inserting the same 
od['a'] = 1
  
print('\nAfter re-inserting') 
for key, value in od.items():  
    print(key, value)



# 3. DefaultDict
#  default_factory is a function that provides the default value for the dictionary created.
#  If this parameter is absent then the KeyError is raised.
# Defining the dict  
print("DefaultDict-------------")
d = defaultdict(int)  
     
L = [1, 5, 3, 4, 5, 4, 1, 5]  
     
# Iterate through the list  
# for keeping the count  
for i in L:  
         
    # The default value is 0  
    # so there is no need to   
    # enter the key first  
    d[i] += 1
         
print(d)

# ChainMap
# A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.
print("ChainMap-----------")
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
  
# Defining the chainmap  
c = ChainMap(d1, d2, d3)  
     
print(c)
# NamedTuple
# DeQue
# UserDict
# UserList
# UserString

