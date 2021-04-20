is_female = True
is_tall = False

if is_female and is_tall :
    print("You are a tall female")

elif  is_female and not(is_tall) :
    print("You are a short female")

elif not(is_female) and is_tall:
    print("You are tall male")

else :
    print("You are a short male")



def max_num(num1,num2,num3) :
    if num1 >= num2 and num1 >=num3:
        return  "num1 is greatest num : " , num1
    elif num2 >= num1 and num2 >=num3:
        return "num2 is the biggest: " , num2
    else :
       return "num3 id the biggest: " , num3


print(max_num(9,5,60))


# I wake up
# If I am hungry
#    I eat Breakfast
#
# I leave my house
# if it's cloudy
#     I bring an umbrella
# otherwise
#     I bring sunglasses
#
# I am at a restaurant
# If I want meat
#      I order Steak
# otherwise If i want pasta
#      I order Sphagetti
# otherwise
#     I order Salad