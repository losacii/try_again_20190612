# lists
keys = ["name", "age", "pay", "job"]
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']
tom = ("Tom", 50, 0, None)

print(bob[0].split()[-1])

people = [bob, sue]
pays = [person[2] for person in people]

print(pays)

NAME, AGE, PAY, JOB = range(4)
print("-->", bob[NAME])


# zip(list, list)  ---> dict
dict_bob = dict(zip(keys, bob))
dict_sue = dict(zip(keys, sue))

# dict of dicts
db = {}
db['bob'] = dict_bob
db['sue'] = dict_sue

print(db['sue']['pay'])

# key & value
for key in db:
    print(key, '--->', db[key])

for key in dict_bob:
    print(key, '--->', dict_bob[key])

print(dict_bob.items())