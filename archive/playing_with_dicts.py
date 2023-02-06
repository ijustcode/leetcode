# phone_book = dict([("Alice", "555-1234"), ("Bob", "555-5678"), ("Charlie", "555-9012")])
# print(type(phone_book))
# print(phone_book)


my_dict = {}
print(type(my_dict))
my_something = {2,3,9}
print(type(my_something))


my_dict["aaaii"] = 118
my_dict["alk"] = 11
my_dict["iakki"] = 22

for i in my_dict:
    print(my_dict[i])



def fibon(n: int) -> int:
    if n == 0 or n == 1:
        return n
    else:
        return fibon(n-1) + fibon(n-2)
