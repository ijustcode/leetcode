# string = "Hello, World!"
# substrings = [string[i:i+n] for i in range(len(string)-n+1) for n in range(1, len(string)-i+1)]
# print(substrings)


my_set = set()
my_set.add(5)
print(my_set)
my_set = {1,2,3}
print(my_set)
my_set.add(5)
print(my_set)

my_set = set([11,22,55])
print(my_set)

my_set.update([33,22])
print(my_set)


(my_set.remove(11))
print(my_set)


my_dict = {'1': 3, '5': 11, '18': 27}
lkj = []
for i in my_dict:
    lkj.append(my_dict[i])
print(lkj)