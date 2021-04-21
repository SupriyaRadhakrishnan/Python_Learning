print(2**3) #Exponents


def expo(base,power) :
    result = 1
    for count in range(power):
        result = result*base
    return result


print(expo(3,4))