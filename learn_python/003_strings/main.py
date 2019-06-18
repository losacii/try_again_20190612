s = "Nam ne quem eros accusata. Pri minim graecis euripidis an. Quem mnesarchum id"
print(s.upper())


words = s.split()
print(words)


print("negative index ---> ", words[-1], words[-2])

x = s[:3]
y = s[4:]
z = "Janefer"[1:-1]


# find, rfind, index, replace

print(dir(str))


# format a string
first = 'John'
last = 'Smith'
a = f"{first} {last} is a coder."
b = "{} {} is a coder".format(first, last)


# len
print(len(words))

# join
x = "~".join(words);    print(x)

# center, rjust, ljust

# replace
s = "Python for beginers"
x = s.replace("beginers", "absolute beginers")

# in operator
res = "for" in s