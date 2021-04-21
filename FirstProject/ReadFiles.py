employee_file = open("employees.txt","r") #r - read , w - write , a - append , r+ - read and write
#print(employee_file.readable())
#print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readlines()[2])

for employee in employee_file.readlines():
    print(employee)

employee_file.close()

# employee_append = open("employees.txt","a")
# employee_append.write("\nToby - Customer Service")
# employee_append.close()

employee_write = open("employees1.txt","w")
employee_write.write("\nToby - Customer Service")
employee_write.close()