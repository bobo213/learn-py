__author__ = 'liubo'
movies = ["The Holy grail",1971,"the life of brian",1973,"the meaning of life",1975]
print(movies[1])

cast = ["clesse","Palin","Jones","Idle"]
print(cast)
print(len(cast))
print(cast[1])

cast.append("Gilliam")
print(cast)

cast.pop()
print(cast)

cast.remove("Palin")
print(cast)

cast.insert(2,"bobobobobobobo")
print(cast)

cast.insert(1,"1971")
cast.insert(3,"1973")
cast.insert(5,"1975")
cast.insert(7,"1977")
print(cast)
print("-------------------")
for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)

print("-------------------")

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)
print_lol(movies)