secretword = "Giraffe"
guess = ""
tries = 0

while guess != secretword  and tries < 3:
     guess = input("Enter the secretword : ")
     tries = tries+1

if(guess == secretword):
 print("You Win!")
else :
     print("You Lost!")
