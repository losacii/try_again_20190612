# coding: utf-8

d = dict()
d["name"] = "John Smith"

dy = {"age": 23}
d.update(dy)

print(d.keys())
print(d.values())
print(d.items())

d3 = {
    'name': 'Susan',
    'age': 29,
    'salary': 5000,
    'score': 8.99
}

d3['job'] = 'sacretary'

d3.pop('age')
print(d3.keys())
print(d3.values())
print(d3.items())

for i in d3.items():

    print("\n----->")
    for j in i:
        print(j)

# ZIP a dictionary
X = ["name", "age", "salary"]
v1 = ["Sue", 22, 4300]
v2 = ["Karl", 38, 5000]

d4 = dict(zip(X, v1))
d5 = dict(zip(X, v2))

print(d4, d5)

print("Done")