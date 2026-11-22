# {}

# Unordered ---> indexing kore value pawa jay na
# immutable ---> no update
# No Duplicates

a = [1, 2, 3, 4, 4, 4, 5]
s = set(a)
#s[0] = 100  # error
print(s)

#Union , Intersection

a = {1, 2, 3}
b = {2, 3, 4}

c = a.intersection(b)
d = a.union(b)
print(c)
print(d)