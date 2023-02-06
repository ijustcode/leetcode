new_set = {2,3,4,8}

li = []

li.append(2)
li.append(4)
li.append(88)

print(f'list: {li} and set is {new_set}')

for i in li:
    new_set.add(i)

print(f'updated set {new_set}')

