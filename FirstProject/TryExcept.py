


try:
  number = int(input("Enter a number :"))
  print(number)
  value = 10 / 0
except ValueError:
    print("Invalid Input")
except ZeroDivisionError as err:
    print("Divided By Zero")
    print(err)