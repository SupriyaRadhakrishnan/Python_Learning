num1 = float(input("Enter the first num : "))
operator = input("Enter the operator : ")
num2 = float(input("Enter the second num : "))

if(operator == "+") :
    print(str(num1) +"+"+ str(num2) + " : " , num1+num2)
elif(operator == "-") :
    print(str(num1) +"-" +str(num2) + " : ",num1-num2)
elif(operator =="*") :
    print(str(num1) +"*" + str(num2) + " : " ,num1*num2)
elif(operator == "/") :
    print(str(num1) +"/" +str(num2) + " : ",num1/num2)
elif(operator == "%") :
    print(str(num1) +"%" + str(num2) + " : " ,num1%num2)
else :
    print("Invalid Operator")