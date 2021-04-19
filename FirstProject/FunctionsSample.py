
def say_hello() :
    print("Hello User")

#Passing Parameters
def say_hello_to(name) :
    print("Hello " + name)

def print_profile(name,age) :
    print("Name : " + name + ". Age : " , age )

def print_friends(friends) :
    print("Friends : " , friends)

#with return statement
def cube(num) :
    return num*num*num


say_hello()
say_hello_to("Jim")
print_profile("Mike",73)
friends = ["Anne","Bruce"]
print_friends(friends)
print(cube(3))
result  = cube(4)
print(result)




