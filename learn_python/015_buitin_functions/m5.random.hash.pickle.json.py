# coding:utf-8
''' ~~~~~~~~~~> random
import os
import random

# print( random.random() )
# print( random.randint(1, 2) )
'''

''' ~~~~~~~~~> hashlib
import hashlib

h = hashlib.md5()
h.update('admin2'.encode('utf8'))
print( h.hexdigest() )
'''

''' ~~~~~~~~~> pickle, json
import pickle

li = range(5, 9)

serialized_obj = pickle.dumps(li) # serial
deserialized_obj = pickle.loads(serialized_obj) # restore

## to file
#pickle.dump(li, open(filepath, 'w')) 

## from file
#pickle.load(open(filepath, 'r') 

print(serialized_obj)
print(deserialized_obj)
# pickle only in python, json in many languages
# xml is being replaced by json / pickle
'''