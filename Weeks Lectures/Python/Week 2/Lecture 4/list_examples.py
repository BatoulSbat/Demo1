colour_list = ["blue", "Orange", "lavender", "cyan"]
colour_list.sort(key = str.lower) # sort the list in alphabetical order
print(colour_list)

colour_list.reverse()
print(colour_list)

#joining list
l1 = ['a', 'b', 'c']
l2 = [1,2,3]
print(l1 + l2)

#using append
for x in l2:
    l1.append(x)

print(l1)

#using extend
l1 = ['a', 'b', 'c']
l1.extend(l2)
print(l1)

#example
newlist = []

for x in colour_list:
    if "a" in x:
        newlist.append(x)

print(newlist)